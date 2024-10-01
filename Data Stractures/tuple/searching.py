my_tuple = 1,2,3,4,5,6,7;
# 1) In Operator: checks if an item is in the tuple
# print(1 in my_tuple) # True
# print(8 in my_tuple) # False

# 2) Looping through a tuple
def search(p_tuple, p_query):
    for index, value in enumerate(p_tuple):
        if value == p_query:
            return index;
    return f"{p_query}, does exist"

five = search(my_tuple, 5);
ten = search(my_tuple, 10);

print(five, "\n", ten);