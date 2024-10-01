# Group Value Types

# A function that takes a list and returns a dictionary with the keys as the type of the values and the values as a list of the values.
# Ex [10, "One", True, 20, "Two", False] -> {int: [10, 20], str: ["One", "Two"], bool: [True, False]}

def group_types(lst):
    result = {}
    # REgister all types in the array
    for el in lst:
        if type(el) not in result:
            result.setdefault(type(el), [])
    # Populate types with values from the list
    
    for key in result.fromkeys():
        for el in lst:
            if type(el) == key:
                result[key].append(el)
    return result
    

    return result;

print(group_types([10, "one", "two", "ten", 20,30,"Five",40, "nine", 50, True]))