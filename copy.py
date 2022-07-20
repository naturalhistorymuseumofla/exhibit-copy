from pathlib import Path
import argparse


def main(old_string, new_string, dir):
    renames = {}
    dir = Path(dir[0])
    if dir.exists():
        paths = [x for x in dir.glob(f'**/{old_string}*')]
        paths.insert(0, dir.resolve())
        for path in paths:
            if path.parent in renames.keys():
                new_path = (renames[path.parent]).joinpath(f'{new_string}' + path.name[3:])
            else:
                new_path = path.parent.joinpath(f'{new_string}' + path.name[3:])
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
        nargs='*',
        default='.'
    )
    args = parser.parse_args()
    main(**vars(args))
