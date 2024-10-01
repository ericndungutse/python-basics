# --------------- SLICING STRING -------------------
# :(Slice operator)
new_string = "Hello Python"
# Excludes the last index
print(len(new_string[0:5]))  # Output: Hello
print(new_string[:5])  # Output: Hello
print(new_string[1:])  # Output: elloPython
print(new_string[6:])  # Output: Python
print(new_string[:])  # Output: Hello Python

# ########## SUM of all the numbers in a string ##########
def sum_of_two_digits(num):
    # print(num)
    first_number = str(num)[0]
    second_number = str(num)[1]
    
    sum = int(first_number) + int(second_number)
    print(sum)

sum_of_two_digits(24);

fruit = 'orange'
for chr in fruit:
    print(chr)

print("***********")
index = len(fruit) -1


print("***********")

while index >=0:
    print(fruit[index]) 
    index = index - 1
    
import random
def count_letter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    print(count, random.sample([1,2,3,4,5,6,7,8,9,10], 3))

count_letter("Eric", "r")

# **************** STRING OPERATORS *****************
# 1) in Operator
print('a' in 'banana')  # Output: True
print('seed' in 'banana')  # Output: False
# 2) not in Operator
print('a' not in 'banana')  # Output: False

# NB: They Are Immutable: Strings are immutable, which means they cannot be changed after they are created.
def firsr_last_characters(word):
    if len(word) < 2:
        return ''
    return word[:2] + word[-2:]

print(firsr_last_characters("jessica"))


# **************** String Methods ************************8
my_name="elshad";

# dir: all methods of a string
print(dir(my_name))
help(my_name.capitalize) #  Return a copy of the string converted to uppercase.
help(my_name.upper) # Return a copy of the string converted to uppercase.
print(my_name.upper())  # Output: ELSHAD
print(my_name.capitalize())  # Output: Elshad

# ****** IMPORTANT STRING METHODS *************
# Sure! Here is a list of the most important string methods in Python:

# 1. **`str.lower()`**: Converts all characters in the string to lowercase.
# 2. **`str.upper()`**: Converts all characters in the string to uppercase.
# 3. **`str.capitalize()`**: Capitalizes the first character of the string and converts the rest to lowercase.
# 4. **`str.title()`**: Capitalizes the first character of each word in the string.
# 5. **`str.strip()`**: Removes leading and trailing whitespace (or other specified characters).
# 6. **`str.lstrip()`**: Removes leading whitespace (or other specified characters).
# 7. **`str.rstrip()`**: Removes trailing whitespace (or other specified characters).
# 8. **`str.split(sep=None, maxsplit=-1)`**: Splits the string into a list of substrings based on a separator.
# 9. **`str.join(iterable)`**: Joins an iterable of strings into a single string with the original string as the separator.
# 10. **`str.replace(old, new, count=-1)`**: Replaces occurrences of a substring with another substring.
# 11. **`str.find(sub, start=0, end=-1)`**: Returns the lowest index where the substring is found, or -1 if not found.
# 12. **`str.index(sub, start=0, end=-1)`**: Similar to `find()`, but raises a `ValueError` if the substring is not found.
# 13. **`str.count(sub, start=0, end=-1)`**: Returns the number of non-overlapping occurrences of the substring.
# 14. **`str.startswith(prefix, start=0, end=-1)`**: Returns `True` if the string starts with the specified prefix.
# 15. **`str.endswith(suffix, start=0, end=-1)`**: Returns `True` if the string ends with the specified suffix.
# 16. **`str.isalpha()`**: Returns `True` if all characters in the string are alphabetic.
# 17. **`str.isdigit()`**: Returns `True` if all characters in the string are digits.
# 18. **`str.isalnum()`**: Returns `True` if all characters in the string are alphanumeric.
# 19. **`str.isspace()`**: Returns `True` if all characters in the string are whitespace.
# 20. **`str.format(*args, **kwargs)`**: Formats the string using the given arguments.

print(my_name.find('d'))  # Output: 5
# search from third index
print(my_name.find('a', 3))  # Output: 4
# search from third index and end at 4 index
print(my_name.find('a', 3, 4))  # Output: 4
line = " Here we go  "
print(line)
# Removes leading and trailing whitespace
print(line.strip())  # Output: Here we go

# Replace: Returns new string
print("I love Python.".replace(".", "!"))
# With counter: Replaces all occurrences of the substring
print("I love Python.....".replace(".", "!"))
# With counter: Replaces the first 2 occurrences of the substring
print("I love Python.....".replace(".", "!", 2))

# ***************** STRING PASSING ***************************
# Extract the domain
data = 'From example.email@edu.co.uk Sat Sep 5 09:14:16 2021'
at_index = data.find('@')
print(data[at_index:data.find(" ", at_index)]) # Output: @edu.co.uk

# Split: COnvert to list: split("<seperator>") default: " ". maxsplit= EX 1. seperate once
print(data.split())  # Output: ['From', '...']
print(data.split(" ", 1))  # Output: ['From', 'example.email@edu.co.uk Sat Sep 5 09:14:16 2021']

split_data = data.split(); 
# JOIN: Convert to string
print(" ".join(split_data))  # Output: From example.email@edu.co.uk Sat Sep 5 09:14:16 2021
print("_".join(split_data))  # Output: From_example.email@edu.co.uk_Sat_Sep_5_09:14:16_2021
print("*".join(split_data))  # Output: From*example.email@edu.co.uk*Sat*Sep*5*09:14:16*2021

# ************ ESCAPE SEQUENCE ***********
question = "He said \t \"What is your name?\""
print(question)  # Output: He said " What is your name?"
question = "He said \t \"What is your name?\""
# C:\Python\nib
print("C:\\Python\\nib") # C:\Python\nib
print(r"C:\Pythion\nib") # C:\Pythion\nib

# ***************** STRING FORMATING **********************
error_no = 56475476823
name = 'Edy'
# Want: Hey Edy, there is a 0xa9834834ce2 error!

# 1) Old Formatting (%)
# s - string, d - decimal, x - hexadecimal
print("Hello, %s" %name) # Output: Hello, Edy
print("Error: %x" %error_no) # Output: Error: 1a2b3c4d

# Want: Hey Edy, there is a 0xa9834834ce2 error!
print("Hey %s, there is a 0x%x error!" %(name, error_no))  # Output: Hey Edy, there is a 0x56475476823 error!

# With Mapping
print("Hey %(name)s, there is a 0x%(error_no)x error!" %{"name": name, "error_no": error_no})  # Output: Hey Edy, there is a 0x56475476823 error!

# str.format()
# Want: Hey Edy, there is a 0xa9834834ce2 error!
print('Hello, {}'.format(name)) # Output: Hello, Edy
print("Hello {}, there was a 0x{:x} error!".format(name,error_no))
# with Mapping
print("Hello {name}, there was a 0x{error_no:x} error!".format(name=name, error_no=error_no))

# ************** F-String **************
print(f"Hello {name}, there was a 0x{hex(error_no)} error!")  # Output: Hello Edy, there was a 0x0xa9834834ce2 error!
print(f"Hello {name}, there was a {error_no:#x} error!")  # Output: Hello Edy, there was a 0x0xa9834834ce2 error!