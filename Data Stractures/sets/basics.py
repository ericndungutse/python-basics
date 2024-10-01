# Store set of unique elements of different types

# NB: Elements should be immutable


fruits = {"apple", "pear", "limon", "grape", "orange"}
fruits2 = {"apple", "pear", "limon", "grape", "orange"}
vegetables = set(["carrot", "potato", "onion", "tomato", "cucumber"])
veg2 = set(tuple(["carrot", "potato", "onion", "tomato", "cucumber"]))

for fruit in fruits:
    print(fruit)

print(fruits, vegetables, veg2, sep="\n")

print(fruits == fruits) # True

# More efficient than list. Higly optimized for membership tests
# In List, membership test is O(n) while in set it is O(1)
# In Set, element is passed through hash function to get hash value, then it is compared with hash value of elements in set
print("apple" in fruits) # True
print("apple" not in fruits) # False

# EMPTY SET
empty = set();
empty2 ={*""};


# ___ADDING ELEMENTS___
my_set = set();
my_set.add(1);
my_set.add(2);
my_set.add(3);
print(my_set); # {1, 2, 3}

# _______ Remove ELements _____
# 1) remove() - Removes element from set. If element is not present, raises KeyError
# 2) discard() - Removes element from set. If element is not present, does nothing
# 3) pop() - Removes and returns an arbitrary element from set. If set is empty, raises KeyError
# 4) clear() - Removes all elements from set

