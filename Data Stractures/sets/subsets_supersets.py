# Finding Subsets of a set: In other words every element in the subset is in the set
animals = {"Dog", "Horse", "Cat", "Robin", "Swallow"};
birds = {"Robin", "Swallow"};

# Check if birds is a subset of animals
result = birds.issubset(animals);
print(result); # True

# Way 2
result = birds <= animals;
print(result); # True

# A set is a subset of itself
result = birds.issubset(birds);
print(result); # True

# Proper Subset: A set is a proper subset of another set if it is a subset of the other set and the two sets are not equal


# FInding a supersset of a set: In other words, every element in the set is in the superset
animals = {"Dog", "Horse", "Cat", "Robin", "Swallow"};
birds = {"Robin", "Swallow"};
result = animals.issuperset(birds);
print(result); # True

# Way 2
result = animals >= birds;
print(result); # True

# Do they have same elements in comoon
result = animals.isdisjoint(birds);
print(result); # False: Which means they have elements in common
# If no common elements, returns True
