my_tuple = 1,2,3,4,5;
my_tuple1 = (6,7,8,9,10);

# 1) Concatenation
results = my_tuple + my_tuple1;
print(results); # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 2) Repetition (*)
tuple_one = (1,);
results = tuple_one * 5;
print(results); # (1, 1, 1, 1, 1)

# 3) In operator

# 4) Slicing
my_tuple = 1,2,3,4,5,6,7,8,9,10;
results = my_tuple[1:5];
print(results); # (2, 3, 4, 5)

# METHODS
# 1) Count Method
my_tuple = 1,2,3,4,5,6,7,8,9,10,10,19;
tens = my_tuple.count(10);
sixes = my_tuple.count(6);
print(sixes); # 1
print(tens); # 2

# 2) Index Method
index = my_tuple.index(6);
print(index); # 5

# BUILT-IN FUNCTIONS
# 1) len()
length = len(my_tuple);
print(length); # 12

# 2) max()
maximum = max(my_tuple);
print(maximum); # 19

# 3) min()
minimum = min(my_tuple);
print(minimum); # 1

# 4) sum()
summation = sum(my_tuple);

# 5) tuple()
# Convert a list to a tuple
my_list = [1,2,3,4,5];
my_tuple = tuple(my_list);
