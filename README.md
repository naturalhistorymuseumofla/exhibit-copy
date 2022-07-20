# exhibit-copy
Copies a directory and all of its child subdirectories/files with a specified string prefix. 

## Download
<a href="https://github.com/naturalhistorymuseumofla/exhibit-copy/raw/main/macOS/copy.zip"><img src="/images/macos-download.svg" width="200px"></a>
<a href="https://github.com/naturalhistorymuseumofla/exhibit-copy/raw/main/Windows/copy.exe"><img src="/images/windows-download.svg" width="200px"></a>

## Usage
Exhibit copy is a command line tool. To use it, first download the appropriate file for your operating system. Then open either Terminal (macOS) or Command Prompt (Windows). You'll then enter in three entries, all seperated by space as below: 
```
<PATH_TO_COPY_FILE> <STRING_TO_FIND> <STIRNG_TO_REPLACE> <PATH_TO_DIRECTORY>
```
The fourth entry, `<PATH_TO_DIRECTORY>` is optional. Without that argument, it will search the current directory. 

### Example
The following command...
```
copy.exe ABC XYZ
```
...will produce the following output:
```    
BEFORE                              AFTER
======                              =====
.                                   .
└── ABC Exhibit                     └── XYZ Exhibit   
    ├── ABC Photos                      ├── XYZ Photos
    │   └── ABC.jpg          -->        │   └── XYZ.jpg
    ├── ABC File                        └── XYZ File   
    │    └── ABC_file.txt                   └── XYZ_file.txt
    └── ABC File                    
        └── Other.txt
 ```

