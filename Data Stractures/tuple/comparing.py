tuple_1 = 0,1,2;
tuple_2 = 0,2,1;

# Compare individual elements
print(tuple_1 == tuple_2) # False
print(tuple_1 < tuple_2) # True
print(tuple_1 > tuple_2) # False

def order_words(p_text):
    results = []
    results_tuple = ()
    words = p_text.split();
    
    for  word in words:
        results.append((len(word), word))
    
    # Sorts by comparing the tuples. First elements of tuple are compared, and the higher one is returned.
    # print(results) # [(6, 'Python'), (2, 'is'), (2, 'my'), (8, 'favorite'), (11, 'programming'), (8, 'language')]
    results.sort()
    
    for value in results:
        results_tuple += value[1],
    return tuple(results_tuple )
    
print(order_words("Python is my favorite programming language"))