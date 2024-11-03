# Os module is used to interact with the operating system
import os
from datetime import datetime

# ************* CHALLENGES *************
# 1. Number of files in a directory
entries = os.scandir("file");
total_files = 0;
for entry in entries:
    if entry.is_file():
        total_files += 1;
print(total_files); # 0

# JOin Path
path = os.path.join("folder1", "folder2", "file.txt");
print(path); # folder1\folder2\file.txt

# Paths
absolutePath = os.path.abspath("file/main.py");
print(absolutePath); # C:\Users\user\Documents\Python\file\main.py

# RElative paths
relativePath = os.path.relpath("file/main.py", "./");
print(relativePath); # ..\file\main.py

# dirname- RETurns the directory name of the path
dirname_name = os.path.dirname("file/main.py");
print(dirname_name); # file

# Basename- Returns the base name of the path - last part of the path
basename_name = os.path.basename("file/main.py");
print(basename_name); # main.py

# EXISTS -PATH
exists = os.path.exists("file/main.py");
print(exists); # True

# cHEck is FILE
isFile = os.path.isfile("file/main.py");
print(isFile); # True

# CHECK IS DIRECTORY
isDirectory = os.path.isdir("file/main.py");
print(isDirectory); # False

# GET SIZE OF A FILE
size = os.path.getsize("file/main.py");
print(size); # 0


# *** DISPLAY CURRENT WORKING DIRECTORY PWD ***
def display_current_working_directory():
    cwd = os.getcwd();
    print("Current working directory: {0}".format(cwd))

# *** CHANGE DIRECTORY CD ***
def up_one_directory_level():
    # chdir: change directory / cd command in terminal
    # Relative path (../)
    os.chdir("../")
    display_current_working_directory()
    
# *** LIST DIRECTORY LS ***
def display_entries_in_directory(directory = '.'):
    # listdir: list directory / ls command in terminal
    # entries = os.listdir(directory);
    entries = os.scandir(directory);
    # scandir() returns an iterator of os.DirEntry objects
    # os.DirEntry objects have the following attributes:
    # name: the name of the entry
    # ALTERNATIVE: entries = os.listdir() returns a list of strings of the names of the entries in the directory path given as an argument to listdir()
    

    for entry in entries:
        print(entry.name, end=" ")
        info = entry.stat()
        print(format_datetime(info.st_mtime))
        print(f"Size: {info.st_size} bytes")
        # OUTPUT
        # .git
        # .gitignore
        # .vscode
        # Basics
        # Data Stractures
        # error_handling
        # file
        # projects
        # recursion
        # Screenshot (545).png

# *** FILE INFORMATION ***
def format_datetime(timestamp):
    utc_timestamp = datetime.fromtimestamp(timestamp);
    formated_timestamp = utc_timestamp.strftime("%d %b %Y %H %M %S");
    return formated_timestamp;

# print(format_datetime(datetime.now().timestamp()));

# up_one_directory_level()
# display_current_working_directory()
# Dsiplays the current working directory
# display_entries_in_directory()
print("***************************************")
# Dsiplays the entries in the directory given as an argument
# display_entries_in_directory('../')
# 
# display_entries_in_directory()
    