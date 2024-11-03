import os

# OBJECT_ORIENTED FILE SYSTEM SYSTEMS
# OPS ARE MORE EFFICIENT THAN OS MODULE OPERATIONS
# MORE DATA RETURNED, NOT JUST A STRING
from pathlib import Path
import glob
# Utility functions for copying and archiving files and directory trees. XXX The functions here don't copy the resource fork or other metadata on Mac.
import shutil

# Archive files
# for file in glob.glob("*.txt"):
#     new_path = os.path.join("archive", file)
#     print(f"Moving {file} to {new_path}")
#     shutil.copy(file, new_path)
# print("Files archived")



# Current working directory
# THis is an object that represents the current directory, unlike os.getcwd() which returns a string
current_path = Path.cwd();

print(Path("file").exists())
print(Path(r"DEv env 1/python"))

# Print home directory
print(Path.home())

# Join
joined_path = Path.home().joinpath("new_dir/test")

print(joined_path)
print (type(joined_path)) # <class 'pathlib.WindowsPath'>

# Access txt from archive
path_test = Path.cwd() / "archive" / "test.txt"
print(path_test) # E:\Dev Env 1\python\file\archive\test.txt

# ------------------- PROPERTIES -------------------------
# FIle Name
print(path_test.name) # test.txt

# FIle stem - name without extension
print(path_test.stem) # test

# FIle suffix - extension
print(path_test.suffix) # .txt

# Directory name
print(path_test.parent) # E:\Dev Env 1\python\file\archive

# PARENT PARENT
print(path_test.parent.parent) # E:\Dev Env 1\python\file

# List files
def display_dir_content():
    entries = Path.cwd()
    for entry in entries.iterdir():
        print(f"File: {entry.name}")   
        print(f"File folder: {entry.parent}")   
        print(f"File name wt ex: {entry.stem}")   
        print(f"File w ex: {entry.stem}")
        print()

display_dir_content()

# GLobal in pathlib
path= Path.cwd()
# returns a list
file_names = path.glob("*.py")

for file_name in file_names:
    print(file_name)


# I GLOB
# GLobal in pathlib
path= Path.cwd()
# returns a list
file_names = path.glob("**/*.py")

for file_name in file_names:
    print(file_name)
    
# OPERATING SYSTEM SPECIFIC


