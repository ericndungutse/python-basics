items = {
    "computer": 10,
    "printer": 50,
}
# # Throws KeyError
# print(items["mouse"])

# print(items["computer"])
# print(items["printer"])

# Method 1: get method returns None if key is not found
quantity = items.get("mouse")
# zero will be returned if key is not found
quantity = items.get("mouse", 0)

quantity = items.get("mouse", "No such item")
print(quantity)

#  SetDefault method
quantity = items.setdefault("computer")
print(quantity) # 10

# Set the missing key to the second parameter if not present, sets it to None
quantity = items.setdefault("mouse", 4)
print(quantity,items) # 10
