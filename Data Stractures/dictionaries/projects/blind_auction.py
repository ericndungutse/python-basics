import os

bidders = {}
another_bidder = "Y"

while  another_bidder.lower() == "y":
    os.system("cls")
    name = input("What is your name?: ")
    bill_amount = int(input("What is your bid?: $"))
    bidders.update({bill_amount: name})
    another_bidder = input("Are there any other bidders?(Y/N)")

# Determine the bidder with the highest bid
bids = list(bidders.keys());
highest_bid = max(bids)


print(f"The winner is {bidders[highest_bid]} with a bid of ${highest_bid}")
    
    