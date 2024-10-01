import random

# 

def print_map(p_map):
    for row in p_map:
        for row in row:
            print(row, end="")
        print("")
        
    
map1 = [["⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜"]]

print("This is the initial map.");
print_map(map1)


# Generate coordinates for golden star on our map
# These are coordinates a user will have to guess
gold_hoizontal = random.randint(0,2);
gold_vertical = random.randint(0,2);

map1[gold_hoizontal][gold_vertical] = "⭐";

gold_position = str(gold_hoizontal +1) + str(gold_vertical+1);


guess=input("Guess the position of the golden star on the map. Enter two digits: ");

if(guess == gold_position):
    print("You found the golden star. You win!");
    print_map(map1);
else:
    print("You missed! Try again");
    map1[int(guess[0])-1][int(guess[1])-1] = "❌";
    print_map(map1);






# Or
# def print_map_two(p_map):
#   joined_nested_rows = [" ".join(row) for row in p_map] 
# #   print(joined_nested_rows) # ['⬜⬜⬜', '⬜⬜⬜', '⬜⬜⬜']
  
#   final_map = " \n ".join(joined_nested_rows)
  
#   print( final_map) # ⬜⬜⬜*⬜⬜⬜*⬜⬜⬜
  
#     # print("\n".join(["".join(row) for row in p_map]))
#     # for row in p_map:
#     #     print("".join(row))