def factorial(n):
    # Step 3, for invalid input
    assert n >= 0 and int(n) == n, 'The number must be a possitive integer only'
    if n in [0,1]:
        return 1
    else:        
        return n * factorial(n-1);

# print(factorial(4))
# print(factorial(-3))


# Fibonacci Series
def fibonacci(n):
    if n in [0,1]:
        return n;
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(5))

# sum of array elements
def sum_of_array(p_list):
    if not isinstance(p_list, list):
        return -1
    if len(p_list) == 0:
        # THis will be the value returned to the last recursion.
        # Since we are adding and we have emplty list, the returned
        # value should be one that does not alter calculation. 
        # Zero makes sence since adding n to zero is always n
        return 0;
    # or: if len(list) == 0: return list[0]
    else:
        return p_list[0] + sum_of_array(p_list[1:])

print(sum_of_array([1,2,3,4,5]))
print(sum_of_array(3))


# a power b
def power(a,b):
    if b < 0 or not isinstance(a, int) or not isinstance(b,int):
        return 'Invalid inputs'
    if b == 1:
        return a;
    elif b == 0:
        return 1
    else:
        return a * power(a, b-1);
    
print(power(3,3))
print(power(3,0))
print(power(3,1))
print(power("e",1))

# Sum of positive numbers: eX 10 => 30 i.e. 1+2+3+4+5+6+7+8+9
