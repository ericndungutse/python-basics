

items = {
    1:{
        "name": "Computer",
        "quantity": 10,
        "price": 500
    },
    2:{
        "name": "Monitor",
        "quantity": 8,
        "price": 200
    },
    3:{
        "name": "Keyboard",
        "quantity": 5,
        "price": 500
    },
    4:{
        "name": "Mouse",
        "quantity": 0,
        "price": 10
    },
    
    5:{
        "name": "HDMI cable",
        "quantity": 7,
        "price": 20
    },
    6:{
        "name": "DVD Drive",
        "quantity": 5,
        "price": 50
    }
}

print("Please add options from the list below:")
print("***************************************")
for key, value in items.items():
    print(f"{key}: {value["name"]}")
    

    
controller = 1;

cart = {};

while controller != 0:
    option = int(input("> "))
    # Check if option exists
    item = items.get(option, None)
    if option == 0:
        break;
    if item == None:
        print("Invalid option")
    
    if item["quantity"] == 0:
        print(f"{item["name"]} out of stock")
        continue;
    
    # If Item exists in the cart, increment quantity 
    print(f"Adding {item["name"]} to cart")
    item_inCart = cart.get(option, None)
    if item_inCart != None:
        item_inCart["quantity"] += 1
    else:
        cart[option] = {
            "name": item["name"],
            "quantity": 1,
            "price": item["price"]
        }
    
    # Update quantity in items
    item["quantity"] -= 1



    
total_price = 0
for value in cart.values():
    total_price += value["price"] * value["quantity"]

total_price = round(total_price, 2)
print(f"Total price: {total_price}")
print("******************************")
print("Thank you for shopping with us")

