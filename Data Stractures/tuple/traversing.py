# Means Looping over a tuple;
my_tuple = "one", "two", "three"

for value in my_tuple:
    print(value)

# Output
# one
# two
# three

print("__________________________")

# Index
index = 0;
for value in my_tuple:
    print(f"{index}: {value}")
    index += 1
# Output
# 0: one
# 1: two
# 2: three

print("__________________________")

# In Python, enumerate() is a built-in function that adds a counter to an iterable and returns it as an enumerate object. 
for index in enumerate(my_tuple):
    print(f"{index}")

# Output
# (0, 'one')
# (1, 'two')
# (2, 'three')

print("__________________________")
# Hence
for index, value in enumerate(my_tuple):
    print(f"{index}: {value}")
# Output
# 0: one
# 1: two
# 2: three

print("__________________________")

# Manual way
for index in range(len(my_tuple)):
    print(f"{index}: {my_tuple[index]}")

print("__________________________")


# enumarate() start index
# default is 0;
my_username = "ericndungutse"
for index, value in enumerate(my_username, 1):
    print(f"{index}: {value}")

# output
# 1: e
# 2: r
# 3: i
# 4: c
# 5: n
# 6: d
# 7: u
# 8: n
# 9: g
# 10: u
# 11: t
# 12: s
# 13: e


# ********** EXPLANATION **********
# enumerate(my_username, 1) returns a tuple of index and value
# then index, value is UNPACKED FROM THE TUPLE