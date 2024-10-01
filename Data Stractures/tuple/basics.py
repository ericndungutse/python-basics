# Immutable data types unlike lists, once created, cannot be changed
tuple_one = 1,2,3
# tuple = (1,2,3)

print(tuple_one) # (1, 2, 3)

# Tuple with single element
single = (1,)

# Empty tuple
empty = ()

my_tuple = tuple('hello') 
print(my_tuple) # ('h', 'e', 'l', 'l', 'o')

my_tuple_from_list = tuple([1,2,3]) 
print(my_tuple_from_list) # (1, 2, 3)





# __________ Tuple vs List __________
# Tuple is faster than list

# Why Tuples
club = ('Barcelona', 'Spain', 1899)
print(club) # ('Barcelona', 'Spain', 1899)
print(club[0]) # Barcelona
print(club[1]) # Spain
print(club[2]) # 1899

# they are immutable, Use less memory, can be used as keys in dictionaries
club[0] = 'Real Madrid' # TypeError: 'tuple' object does not support item assignment

# Protect data integrity since it is immutable



# **************** Unpacking/Destructuring a tuple  ************
x, y = 1, 2,3 # print(x, y) # 1 2
x, y,z = (1,2,3); print(x, y, z) # 1 2 3

my_names_tuple = ('John', 'Doe')
first_name, last_name = my_names_tuple;

print(first_name, last_name) # John Doe

# **************** Unpacking/Destructuring a list  ************
# Since it is muttable, it is not advicable to unpack a list since you have to unpack all at once
