import argparse
from pathlib import Path
import shutil

def parse_argv():
    parser = argparse.ArgumentParser(description="Копіює файли в папку")
    parser.add_argument("-s", "--sourсe", type=Path, required=True, help="Папка з файлами")
    parser.add_argument("-o", "--output", type=Path, default="dist", help="Папка для копіювання")
    return parser.parse_args()

def recursive_copy(sourse, output):
    for item in sourse.iterdir():
        if item.is_dir():
            recursive_copy(item, output)
        else:
            item_name = item.name.split(".")
            folder = item_name[-1]
            folder = output / folder
            folder.mkdir(exist_ok=True, parents=True)
            shutil.copy(item, folder)

def main():
    try: 
        args = parse_argv()
        recursive_copy(args.sourсe, args.output)
    except OSError:
        print("File or directory can't be read")
        

if __name__ == "__main__": 
    main()