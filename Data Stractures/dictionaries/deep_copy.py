import copy;

city_list = ["Kigali", "Nairobi", "Kampala"]
language_list = ["Kinyarwanda", "Swahili", "Luganda"]
name_list = ["Eric", "John", "Jane"]


person = {
    "name": name_list,
    "city": city_list,
    "language": language_list
}

# SHallow Copy
# new_person = person.copy()

# new_person["city"].append("Dar es Salaam")

# print(id(new_person["city"]), id(person["city"]))
# print(id(new_person), id(person))

# DEEP COPY
new_person = copy.deepcopy(person);
new_person["city"].append("Dar es Salaam")
print(new_person["city"], person["city"])   