custom_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
}

devices_list = ["phone", "tablet", "Computer", "TV"]

# 1) From Keys
new_dict = {}.fromkeys(devices_list)
# new_dict = dict.fromkeys(devices_list)
print(new_dict) #{'phone': None, 'tablet': None, 'Computer': None, 'TV': None}
new_dict = {}.fromkeys(devices_list, 0)
print(new_dict) #{'phone': 0, 'tablet': 0, 'Computer': 0, 'TV': 0}


# 2) Keys
keys = custom_dict.keys()
print(type(keys)) # <class 'dict_keys'>
print(keys) # dict_keys([0, 1, 2, 3, 4, 5, 6])