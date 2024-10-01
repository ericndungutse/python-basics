# _____ UNION _____
fruits = {"apple", "pear", "limon", "tomato","grape", "orange"};
vegetables = {"carrot", "potato", "onion", "tomato", "cucumber"}

fruivegs = fruits.union(vegetables);
print(fruivegs)

# Pipe operator can also be used to perform union
fruivegs = fruits | vegetables;


# ______ INTERSECTION ______
fruits = {"apple", "pear", "limon", "tomato","grape", "orange"};
vegetables = {"carrot", "potato", "onion", "tomato", "cucumber"}

inters = fruits.intersection(vegetables);
inter2 = vegetables.intersection(fruits);
print(inters, inter2)

# And Operator
inters4 = fruits & vegetables;
print(inters4)

# 3) Sets: <set>.intersction_update(<set1>,<set2>,<set3>....) - Updates set with intersection of itself and other sets or set.intersection(<set1>,<set2>,<set3>....)


# __________ SUBTRACTION __________
fruits = {"apple", "pear", "limon", "cocumber","grape", "orange"};
vegetables = {"broccoli", "pepper", "onion", "garlic", "cocumber"};

print(fruits.difference(vegetables));
print(vegetables.difference(fruits));
print(fruits - vegetables);


# ___________ Symetric Difference ___________
# Elements that are in either of the sets but not in both. Union - Intersection

fruits = {"apple", "pear", "limon", "cocumber","grape", "orange"};
vegetables = {"broccoli", "pepper", "onion", "garlic", "cocumber"};

syme_diff = fruits.symmetric_difference(vegetables); # or fruits ^ vegetables

print(syme_diff);


# ___________ Modification Operations ___________

# 1) Union does not modify the original sets

# Modify the original set. This is done by using the update method or the pipe operator
fruits |= vegetables;
vegetables.update(fruits);
print(vegetables); # {'apple', 'pear', 'limon', 'cocumber', 'grape', 'orange', 'broccoli', 'pepper', 'onion', 'garlic'}
print(fruits); # {'apple', 'pear', 'limon', 'cocumber', 'grape', 'orange', 'broccoli', 'pepper', 'onion', 'garlic'}

# 2) Intersection does not modify the original sets
# Update first set with intersection of itself and other sets
set1 = {1, 2, 3, 4, "Two", 5};
set2 = {"Set", "Two", 1}

set1.intersection_update(set2); # {'Two', 1}
print(set1);

# With Ampasand operator
set1 &= set2;


# ___________ Difference ___________
print("*************** Difference ***************")
set1 = {1, 2, 3, 4, "Two", 5};
set2 = {"Set", "Two", 1}
diff = set1.difference(set2); # {2, 3, 4, 5}
print(set1,set2); # They are not modified
# Update wirh difference of itself and other sets
set1.difference_update(set2);
print(set1); # {2, 3, 4, 5}
# OR fruits -= vegetables;


# __________ Sytmetric Difference ___________
print("*************** Symmetric Difference ***************")
# Same as above
set1 = {1, 2, 3, 4, "Two", 5};
set2 = {"Set", "Two", 1}
sym_diff = set1.symmetric_difference(set2); # {2, 3, 4, 5, 'Set', 5}
print(sym_diff);
set1.symmetric_difference_update(set2);
print(set1); # {2, 3, 4, 5, 'Set', 5}
# OR fruits ^= vegetables;