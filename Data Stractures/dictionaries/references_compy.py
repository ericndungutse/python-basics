
# Are Referenced by addresses
person = {
    "name": "Eric",
    "age": 29,
    "city": "Kigali"
}

# Hence
new_person = person # new_person refferes to the same address as person

# ************* Making a different reference with COPY METHOD *************
# deep_copy_person = person.copy() # deep_copy_person is a new address
# print(deep_copy_person)

# |The above is shallow copy since values of the dictionary are immutable

# DIC WITH MUTABLE VALUES
person_two = {
    "names": ["Eric", "John", "Jane"],
    "city": ["Kigali", "Nairobi", "Kampala"],
    "laguage":["Kinyarwanda", "Swahili", "Luganda"]
}

person_two_copy = person_two.copy() # shallow copy

# Since list is also referenced, person_two_copy["city"] and person_two["city"] points to the same address
print(person_two_copy["city"], person_two["city"])

# ****** HERE NO ISSUE ***********
# person_two_copy["city"] = "Kigali" # This will affect only person_two_copy, coz, we change the identifier target
# print(person_two_copy["city"], person_two["city"])

# However, this will affect both, since it is the object being changed
person_two_copy["city"].append("Dar es Salaam");
print(person_two_copy["city"], person_two["city"])
