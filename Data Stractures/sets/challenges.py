# ###################### NUMBERS DIVISIBLE BY 3 and 4 ####################

# # Num Divisible by 3;
# divisible_by_3 = set(range(0, 11, 3));
# print(divisible_by_3);

# # Nums divisible by 4
# divisible_by_4 = set(range(0, 11, 4));
# print(divisible_by_4);

def divisible_by_3_and_4(n):
    set1 = set(range(0, n, 3));
    set2 = set(range(0, n, 4));
    
    print(set1.intersection(set2));

# divisible_by_3_and_4(20);


# ###################### Find Propositions in a quote ####################

quote = """Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do."""
prep = {"as", "but", "by", "for", "in", "of", "on", "to", "with"}

# Use Intersection to find the propositions in the quote

# 1) Ceate set of quote
quote_set = set(quote.split());

# 2) Find intersection of the quote and the prepositions
prop_in_set = quote_set.intersection(prep);

# print(prop_in_set);


# ############# Difference o more than two sets ####################
a = {1, 2, 3, 40, 50, 300, 400}
b = {10, 20, 30, 40, 300}
c = {100, 200, 300, 400}

print(a.difference(b, c));
print(b.difference(a, c));