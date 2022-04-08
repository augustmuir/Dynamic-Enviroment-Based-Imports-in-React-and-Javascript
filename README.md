# Dynamic Enviroment Based Imports in React / Javascript / Node

You can use this method to use different imports dynamically bassed on your target(s). This solution dosen't asynchronous import or bloat your bundle size with any unused code.

In this example I have three targets: iOS, Web, Android. Some files will be for a single target, while some files may target two (for example iOS/Android share a import, while web has it's own).

You can change targets by running a npm script:
`npm run target-android`

Requirements: Python 3

**Warning: This script modifies your source code. You need to backup your source code, and modifiy this code to fit your needs first. This is just a example.**

### How it Works:
Say you have a Typescript project that targets Web, iOS, and Android - and all three platforms have the odd file which is platform specific. Simply use custom extensions to differentiate the files. In the example I am using:

`.tsx` Shared between all targets  
`.ios.tsx` iOS only  
`.android.tsx` Android only  
`.web.tsx` Web only  
`.mobile.tsx` iOS or Android  
`.webandroid.tsx` Web or Android  

You can also use different naming schemes for any other use case you may have such as production vs development:

`example.prod.js`   
`example.dev.js`

### Step 1:
Define how you will name your files and extensions to differentiate what file is for what target. In this example, if there is no additional file extenison, the file will be consdiered shared accross all targets. Add a comment beside dynamic imports so the script can find the line, and know what it's options are.

`import Avatar from "./Avatar.webandroid"; // !dynamic-import options=["webandroid", "ios"]`

In the above example I have the files `Avatar.webandroid.tsx` for Android and Web, and `Avatar.ios.tsx` for iOS.

### Step 2: 
Add a python file under the root of your project `setImportTargets.py`. Copy the code from the python file in this repo, and modify it to fit your needs and file extension scheme. In this example I use components with the same names, but different file extensions. If you want completely diffrent import file names/paths, you will need to modify the script to reflect that.

### Step 3 (optional):
Add scripts to your `package.json` for changing the target:
```
"scripts": {
   ...
   "target-web": "python3 setImportTargets.py web",
   "target-android": "python3 setImportTargets.py android",
   "target-ios": "python3 setImportTargets.py ios"
}
```

### Step 4:
Backup your code before developing/testing your solution! Run the script via npm or python to change your imports.    
`npm run target-ios`  
`python3 setImportTargets.py ios`

The script will output all changes:
```
Line modified in file: ./app/components/profiles/Avatar.tsx
Org: import Avatar from "./Avatar.webandroid"; // !dynamic-import options=["webandroid", "ios"]
New: import Avatar from "./Avatar.ios"; // !dynamic-import options=["webandroid", "ios"]
```




