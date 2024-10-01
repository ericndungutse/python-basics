my_dict = {
    0: 'three',
    5: "five",
    9: "nine",
    2: "two",
    1: "one",
    4: "four",
}

# ________ IN/NOT IN ________
print(0 in my_dict) # True
print(5 not in my_dict) # False
print("five" in my_dict.values()) # True

# _______ len() _______
print(len(my_dict)) # 6

# _______ all() _______
print(all(my_dict)) # True

# __________ sorted() returns a list of sorted keys __________
print(sorted(my_dict)) # [0, 1, 2, 4, 5, 9]