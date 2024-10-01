import random
name_list =[];
name = input("Input everyone's name seperated by comma.");

name_list = name.split(', ');

payer = random.choice(name_list);

print(f"{payer} will pay the bill today");