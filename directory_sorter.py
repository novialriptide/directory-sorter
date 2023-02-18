import argparse
import colorama
import shutil
import sys
import os

parser = argparse.ArgumentParser(prog="Directory Sorter")
parser.add_argument("directory_path")
args = parser.parse_args()

directory_path = args.directory_path
files = []

for x in os.listdir(directory_path):
    if len(x) == 1:
        print(f"Error: cannot sort 1 letter files, please remove: \"{x}\"")
        sys.exit()

    x = os.path.join(directory_path, x)
    if os.path.isdir(x):
        print(f"Error: found a directory, please remove: \"{x}\"")
        sys.exit()

for x in os.listdir(directory_path):
    first_letter = x[0]
    x = os.path.join(directory_path, x)
    print(first_letter)
    target_directory = os.path.join(directory_path, first_letter)
    if not (os.path.exists(target_directory) and os.path.isdir(target_directory)):
        os.mkdir(target_directory)
        
    shutil.move(x, target_directory)
