import os

def top_down_walk_function(path='.'):
    # os.walk() returns a generator object
    for dirpath, dirnames, files in os.walk(path):
        print("Directory path: {0}".format(dirpath))
        print("--------------- INCLUDES THESE DIRECTORIES -----------------")
        print("Dirnames: {0}".format(dirnames))
        print("--------------- INCLUDE THESE FILES ----------------")
        print("Files: {0}".format(files))
        print("--------------------------------")

top_down_walk_function()