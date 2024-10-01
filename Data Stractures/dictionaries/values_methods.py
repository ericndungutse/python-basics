custom_dictionary = {
    0: "zero",
    1: "one",
    3: "three",
    5: "five",
    7: "seven",
}


# .Items()
for value in custom_dictionary.items():
    print(value) # (0, 'zero') (1, 'one') (3, 'three') (5, 'five') (7, 'seven')
    
for ke, value in custom_dictionary.items():
    print(ke, value) # 0 zero 1 one 3 three 5 five 7 seven
    
print(custom_dictionary.items()) # dict_items([(0, 'zero'), (1, 'one'), (3, 'three'), (5, 'five'), (7, 'seven')])

# Challenge
# Length of Dictionary Values
names_dict = {
    1: "Elshad",
    2:"Renad",
    3: "Johanna",
    4: "Appmillers",    
}

def value_legth(dictionary):
    new_dectionary = {}
    
    for key, item in dictionary.items():
        new_dectionary[key] = {item: len(item)}
    return new_dectionary

print(value_legth(names_dict)) # {1: {'Elshad': 6}, 2: {'Renad': 5}, 3: {'Johanna': 7}, 4: {'Appmilliers': 11}}

# ________ UPDATE METHOD __________
custom_dictionary = {
    0: "zero",
    1: "one",
    2: 'two',
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",   
}

second_dict = {
    8: "eight",
    9: "nine",
    1: 'new one',
    2: 'new two',
}

# Updating does not change the position of keys
custom_dictionary.update(second_dict)
for item in custom_dictionary.items():
    print(item) # (0, 'zero') (1, 'new one') (3, 'three') (4, 'four') (5, 'five') (6, 'six') (7, 'seven') (8, 'eight') (9, 'nine')
    
# custom_cict_2 |= second_dict;

# _________ Concantinate 3 Dictionaries __________
dict_1 = {
    1: "one",
    2: "two",
}

dict_2 = {
    3: "three",
    4: "four",
}

dict_3 = {
    5: "five",
    6: "six",
}

# ___________ Values Method ___________
custom_dictionary = {
    0: "zero",
    1: "one",
    2: 'two',
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",   
}

print(custom_dictionary.values()) # dict_values(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven'])
# *************** dic.items() returns a special data structure called view objects *******************