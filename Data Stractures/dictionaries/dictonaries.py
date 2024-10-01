
my_dictionary = {
    "Miller": "a person who owns or works in a corn mill",
    "Programmer":"a person who writes computer programs",
    "App": "an application downloaded by users to a mobile device",
}

# Accessing the value of a key
print(my_dictionary["Miller"]) # Output: a person who owns or works in a corn mill

# __________ EMPTY DICTIONARY __________
my_empty_dictionary = {};
my_empty_dictionary_two = dict();

# _________Clear a dictionary_________
my_dictionary = {}

# TODO _________ INSERT AND UPDATE __________
my_empty_dictionary_two["name"] = "Eric";
my_empty_dictionary_two["age"] = 23;
print(my_empty_dictionary_two) # Output: {'name': 'Eric', 'age': 23}
my_empty_dictionary_two["age"] = 29;
print(my_empty_dictionary_two) # Output: {'name': 'Eric', 'age': 23}

# TODO ________ Traversing Elements in dictionary ___________
print("************* Treversing ***************")

my_dictionary = {
    "Miller": "a person who owns or works in a corn mill",
    "Programmer":"a person who writes computer programs",
    "App": "an application downloaded by users to a mobile device",
}

# Loops through keys
for key in my_dictionary:
    print(key, ":", my_dictionary[key])
    
    
def multipy_values(my_dict):
    product = 1;
    for key in my_dict:
        product *= my_dict[key];
        
    return product;

print(multipy_values({"one":1, "two":2, "three":3, "four":4}));

# Scores
students_scores = {
    "John": 90,
    "Edy": 68,
    "Marry": 88,
    "Ewan": 79,
    "Park":62,
    "Keza": 30,
}

def convert_grade(scores):
    output = {}
    for key in scores:
        output[key]="Outstanding" if scores[key] >= 85 else "Good" if scores[key] >= 65 else "Acceptable" if scores[key] >= 50 else "Fail";
    return output;

print(convert_grade(students_scores));

# TODO ------------ remove elements from dictionary ------------
students_scores = {
    "John": 90,
    "Edy": 68,
    "Marry": 88,
    "Ewan": 79,
    "Park":62,
    "Keza": 30,
}

# ***** Pop Method: removes the item with the specified key name and return the removed item
result = students_scores.pop("Keza");
# KeyError: 'Kezaa'
# result2 = students_scores.pop("Kezaa");
# Handle KeyError
result3 = students_scores.pop("Kezaa", "No such key found");
print(students_scores, result3);

# ******* Popitem Method: removes the last item in the dictionary following the LIFO order
print('***************************')
print(students_scores);

result4 = students_scores.popitem();

print(students_scores, result4); #Removes Park

#  ********* del keyword: removes the item with the specified key name
del students_scores["John"];
print(students_scores);

# ((**** clear method: removes all the items in the dictionary ****))
students_scores.clear();
print(students_scores)


# TODO:__________________ Renaming a key _______________________
my_dictionary = {
    "name": "Eric",
    "age":29,
    "salary": 50000,
    "city": "Kigali",
}

my_dictionary["address"] = my_dictionary.pop("city");
print(my_dictionary);

# TODO IN and NOT IN operators
my_dictionary = {
    "name": "Eric",
    "age":29,
    "salary": 50000,
    "city": "Kigali",
}

print("name" in my_dictionary); # Output: True
print("country" not in my_dictionary); # Output: True
print("country" in my_dictionary); # Output: False


# Count words
word = "BABACDAS"
print(list(word));

def count_characters(word):
    output = {};
    for char in word:
        if char not in output:
            output[char] = word.count(char);
    return output;

print(count_characters(word));

# TODO NESTED LISTS
programming_languages = {
    "eric": ["Python", "Java", "C++"],
    "john": ["Java", "C++"],
}
programming_languages = {
    "eric": {
        "fav_languages": ["Python", "Java", "C++"],
        "experience": 10,
        },
    "john": ["Java", "C++"],
}