#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
import argparse


def main(old_string, new_string, dir=None):
    def return_new_path(path):
        '''
        Returns a properly formatted new Path object with proper new location and string prefix
        :param path: Path object to be formatted
        :return: Path object
        '''
        if path.parent in renames.keys():
            parent = renames[path.parent]
        else:
            parent = path.parent
        return parent.joinpath(f'{new_string}' + path.name[3:])

    # Keeps track of new paths
    renames = {}

    if dir:
        dir = Path(dir)
        # If the optional target dir arg is given, add its new filepath to the renames dictionary
        new_dir = return_new_path(dir)
        renames[dir] = new_dir
    else:
        dir = Path('.')

    if dir.exists():
        # Return a list of all paths of dir/files in nested directories 
        paths = [x for x in dir.glob(f'**/{old_string}*')]
        paths.insert(0, dir.resolve())
        for path in paths:
            if path.parent in renames.keys():
                new_path = return_new_path(path)
            else:
                new_path = return_new_path(path)
            if path.is_dir():
                renames[path] = new_path
                new_path.mkdir(parents=True, exist_ok=True)
            else:
                path.replace(new_path)
    else:
        print('The filepath you entered does not seem to exist.')


if __name__ == "__main__":
    description = '''\
Welcome to Exhibit Copy! 
==========================
Create a copy of a directory and all of its child
subdirectories/files, all with a specified letter prefix (see below). 
        
.                                   .
└── ABC Exhibit                     └── XYZ Exhibit   
    ├── ABC Photos                      ├── XYZ Photos
    │   └── ABC.jpg          -->        │   └── XYZ.jpg
    ├── ABC File                        └── XYZ File   
    │    └── ABC_file.txt                   └── XYZ_file.txt
    └── ABC File                    
        └── Other.txt
    '''
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=description)
    parser.add_argument('old_string', help='The old string prefix to search for and copy.')
    parser.add_argument('new_string', help='The new string prefix to be added to the copies files and folders.')
    parser.add_argument(
        'dir',
        help="Optional argument that points to directory where files and folders are to be copied",
        nargs='?',
    )
    args = parser.parse_args()
    main(**vars(args))
