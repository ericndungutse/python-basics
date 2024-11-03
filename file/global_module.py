import glob;

# Scenrio, find all png files in a directory
def display_jpg_files():
    for file in glob.glob("*.jpg"):
        print(file)
        

# Files containing nature in the name
def display_natures():
    for file in glob.glob("*nature*"):
        print(file)
        
# Include subdirectories
def display_natures_subdir():
    fnature_files = glob.iglob("**/*mountain*", recursive=True)
    for file in fnature_files:
        print(file)

# print("----------------------- Displaying all jpg files -----------------------")
# display_jpg_files()

# print("----------------------- Displaying all files containing nature in the name -----------------------")
# display_natures()

print("----------------------- Displaying all files containing mountain in the name including subdirectories -----------------------")
display_natures_subdir()