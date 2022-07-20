# exhibit-copy
Copies a directory and all of its child subdirectories/files with a specified string prefix. 

## Download
<a href="https://github.com/naturalhistorymuseumofla/exhibit-copy/raw/main/macOS/copy.zip"><img src="/images/macos-download.svg" width="200px"></a>
<a href="https://github.com/naturalhistorymuseumofla/exhibit-copy/raw/main/Windows/copy.exe"><img src="/images/windows-download.svg" width="200px"></a>

## Installation 
### macOS
1. Unzip copy.zip
2. Add "copy" file to `/usr/local/bin`
### Windows
1. Open Start menu
2. Type Edit environment variables
3. Open the option "Edit the system environment variables"
4. Click "Environment variables..." button
5. There you see two boxes, in System Variables box find path variable
6. Click Edit
7. Click New
8. Type the Directory path of the copy.exe ( Directory means exclude the file name from path)
9. Click Ok on all open windows and restart Command Prompt.
## Usage
Exhibit copy is a command line tool. To use it, first download the appropriate file for your operating system. Then open either Terminal (macOS) or Command Prompt (Windows). You'll then enter in up to three arguments, all seperated by a space as below: 
```
copy <STRING_TO_FIND> <STIRNG_TO_REPLACE> <PATH_TO_DIRECTORY>
```
The last argument, `<PATH_TO_DIRECTORY>` is optional. Without that argument, it will search the current directory. 

### Example
The following command...
```
copy ABC XYZ
```
...will produce the following output:
```    
BEFORE                              AFTER
======                              =====
.                                   .
└── ABC Exhibit                     └── XYZ Exhibit   
    ├── ABC Photos                      ├── XYZ Photos
    │   └── ABC.jpg          -->        │   └── XYZ.jpg
    └── ABC File                        └── XYZ File   
         │── ABC_file.txt                   └── XYZ_file.txt                 
         └── Other.txt
 ```

