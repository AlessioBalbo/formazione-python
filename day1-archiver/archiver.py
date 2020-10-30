import argparse
import zipfile
import zlib
from os.path import isfile, exists

def main():
    parser = argparse.ArgumentParser(description="create a zip file with given input files")
    parser.add_argument(
        "output",
        type=output_zip_path,
        help="output zip file path")
    parser.add_argument(
        "input",
        type=input_file_path,
        nargs="+",
        help="input file to compress")
    
    args = parser.parse_args()
    
##  print(f"output:{args.output}")
##  print(f"input:{args.input}")          

    if args.output is None:
        return
    
##  ar = zipfile.ZipFile(args.output, mode="w", compression=zipfile.ZIP_DEFLATED)
    
    with zipfile.ZipFile(args.output, mode="w", compression=zipfile.ZIP_DEFLATED) as ar:
        for path in args.input:
            try:
                ar.write(path)
            except OSError:
                print(f"input file '{path}' not readable")
    
    print(f"archive '{args.output}' created")


def output_zip_path(path):
    if not exists(path):
        return path
    elif isfile(path):
        print(f"'{path}' file already exist, it will be deleted, confirm? [Y/n]")
        s = input()
        if s in ("Y", "y"):
            return path
        else:
            print("output file not confirmed")
            return None

def input_file_path(path):
    if exists(path):
        if isfile(path):
            return path
        else:
            raise argparse.ArgumentTypeError(f"input file '{path}' is not a valid file")
    else:
        raise argparse.ArgumentTypeError(f"input file '{path}' does not exist")
    
if __name__ == "__main__":
    main()
