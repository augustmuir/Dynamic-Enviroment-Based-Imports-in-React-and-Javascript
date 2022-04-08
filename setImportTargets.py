import sys
import glob
from ast import literal_eval

def main():
    platform = sys.argv[1]
    print("\nModifying imports to match the specified platform: " + platform + "\n")

    # recursively go through all files
    filepaths = glob.glob("./**/*.tsx", recursive=True)
    for filePath in filepaths:
        fileIn = open(filePath, "r")
        lines = fileIn.read().splitlines()
        fileIn.close()

        # check all lines for !dyanmic-import market
        wasChanged = False
        newLines = []
        for line in lines:
            # if import is dynamic, replace line to use correct import
            if "!dynamic-import" in line:
                wasChanged = True
                options = literal_eval(line.split("options=")[1])
                line = getModifiedLine(filePath, line, platform, options)
            newLines.append(line+"\n")

        #replace file with modified lines
        if wasChanged == True:
            fileOut = open(filePath, "w")
            fileOut.writelines(newLines)
            fileOut.close()
                

def getModifiedLine(filePath, line, platform, options):
    # import Avatar from "./Avatar.ios"; // !dynamic-import options=["webandroid", "ios"]
    originalImportName = line.split('"; // !dynamic-import')[0].split("/")[1] # Avatar.ios
    withoutExtenison = originalImportName.split(".")[0] # Avatar
    newImportName = None

    if platform == "web":
        if "web" in options:
            newImportName = withoutExtenison + ".web"
        elif "webandroid" in options:
            newImportName = withoutExtenison + ".webandroid"
    elif platform == "ios":
        if "ios" in options:
            newImportName = withoutExtenison + ".ios"
        elif "mobile" in options:
            newImportName = withoutExtenison + ".mobile"
    elif platform == "android":
        if "android" in options:
            newImportName = withoutExtenison + ".android"
        elif "mobile" in options:
            newImportName = withoutExtenison + ".mobile"
        elif "webandroid" in options:
            newImportName = withoutExtenison + ".webandroid"

    if newImportName == None:
        print("!!! Error: Dynamic Import Error in file: " + filePath)
        print("!!! Line:" + line)
        return None
    
    beforeImportName = "".join(line.split("; // !dynamic-import")[0].split("/")[0]) + "/"
    afterImportName = '"; // !dynamic-import ' + line.split("!dynamic-import ")[1]
    newLine = beforeImportName + newImportName + afterImportName
    
    print("Line modified in file: " + filePath)
    print("Org: " + line)
    print("New: " + newLine)
    print("-------------------")

    return newLine


main()