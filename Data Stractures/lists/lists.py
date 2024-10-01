countries_of_uk = ["England", "Scotland", "Wales", "Northern Ireland"] # List of strings
names = ["England", "Scotland", "Wales", "Northern Ireland"] # List of integers and strings
# Lists are mutable
names[0] = 20
print(names) # [20, 23, 33, 22, 33, 'England', 'Scotland', 'Wales', 'Northern Ireland']

for name in names:
    print(name) # 20 23 33 22 33 England Scotland Wales Northern Ireland

print(names[0])
# Loop with index
for index in range(0,len(names)):
    print("Index:",index, "Value:", names[index]) # Index: 0 Value: 20 Index: 1 Value: 23 Index: 2 Value: 33 Index: 3 Value: 22 Index: 4 Value: 33 Index: 5 Value: England Index: 6 Value: Scotland Index: 7 Value: Wales Index: 8 Value: Northern Ireland
    # print(names[index]) # 20 23 33 22 33 England Scotland Wales Northern Ireland

# Backword loop
for index in range(len(names)-1, -1, -1):
    print("Index:",index, "Value:", names[index]) # Index: 8 Value: Northern Ireland Index: 7 Value: Wales Index: 6 Value: Scotland Index: 5 Value: England Index: 4 Value: 33 Index: 3 Value: 22 Index: 2 Value: 33 Index: 1 Value: 23 Index: 0 Value: 20
    
print('-----------------------------------------------------------------------')
# ************* LIST OPERATIONS *************

# 1) SLICE
my_list = [1,2,3,4,5,6,7,8,9,10];
print(my_list[0:5]) # [1, 2, 3, 4, 5]
print(my_list[:5]) # [1, 2, 3, 4, 5]
print(my_list[1:]) # [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Replace values
my_list[0:5] = ["A","B","C","D","E"]
print(my_list) # ['A', 'B', 'C', 'D', 'E', 6, 7, 8, 9, 10]
my_list[:2] = ["X","Y", "Replaced","New Added"] # ['X', 'Y', 'Replaced', 'New Added', 'C', 'D', 'E', 6, 7, 8, 9, 10]
print(my_list)
my_list[:5] = [')','?']
print(my_list) # [')', '?', 'D', 'E', 6, 7, 8, 9, 10]
my_list[:5] = []
# Deletes elements from 0 to 4
print(my_list) # [7, 8, 9, 10]

# 2) CONCANTINATION (+ Operator)
list_1 = [1,2,3];
list_2=[4,5,6]
print(list_1 + list_2) # [1, 2, 3, 4, 5, 6]

# 3) Star Operator
list_one = [1];
list_two = list_one * 5
print(list_two) # [1, 1, 1, 1, 1]
list_two[5:8] = ["X","Y","Z"]
print(list_two * 2); # [1, 1, 1, 1, 1, 'X', 'Y', 'Z', 1, 1, 1, 1, 1, 'X', 'Y', 'Z']

# 4) in Operator: Does element exists in the list?
list_my =['a',44,'y',43];
print('a' in list_my) # True
print(3 in list_my) # False

# 5) not in Operator: Does element not exists in the list?
print(3 not in list_my) # True


list_new = ['a','b','c','d', 'e','f']

# from 0 to 5 step -1
print(list_new[::-1]) # ['f', 'e', 'd', 'c', 'b', 'a']

print(list_new[4:1:-1])
print(list_new[0::-1])
 
# ********************* LIST METHODS *********************
animals = ['cat', 'dog', 'bat', 'mouse', 'horse', 'bear']
print(dir(animals)) # ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# 1) index method returns the index of the first occurrence of the value

print(animals.index('cat')) # 0
# Parameters: object:element, start, and stop

# 2) append method adds an element to the end of the list
# Returns None
animals.append('lion');
print(animals)

# 3) extend 
animals_2 = ['fox', 'rabbit']
animals.extend(animals_2) # ['cat', 'dog', 'bat', 'mouse', 'horse', 'bear', 'lion', 'fox', 'rabbit']

# 4) insert method adds an element at a specific index

# 5) remove method removes the first occurrence of the value
# returns None
animals.remove('bat')

# 6) count method returns the number of occurrences of the value
print(animals.count('cat')) # 1

# 7) pop method removes the element at the specified index and returns it
print(animals) # cat
animals.pop(animals.index('cat'))
print(animals) # ['dog', 'mouse', 'horse', 'bear', 'lion', 'fox', 'rabbit']

# 8) Reverse Method: Reverse the list in place and returns None
animals.reverse();
print(animals) # ['rabbit', 'fox', 'lion', 'bear', 'horse', 'mouse', 'dog']

# 9) Sort Method: Sort the list in place and returns None
nums = [20,401,3,2,11,4,5,66,7,38,9,10]
nums.sort();
print(nums) 
descend = sorted(nums, reverse=True)

# 10) Copy
new_animals = animals.copy()

# 11) Clear Method: Removes all elements from the list


# ------------- EXERCISES --------------------------
# 1) Update the first occurance of the value in the list
list1 = [10,56,10,5,15,50,50,20];
print(list1)
index1 = list1.index(50);
second_index = list1.index(50, index1+1);
# list1[index1] = 99;
# print(list1)

# Second occurance
list1[second_index] = 100;


print(list1)

def count_words(words):
    count = 0;
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1;
    return count;

print(count_words(['cbc', 'xyz', 'aba', '2332','abc']))

# ******************* FUNCTION WTH LST *******************
# 1) len function
# 2) max function
# 3) min function
# 4) sum function
print(sum([3,4,1]))
# 5) delete method at a specified index
# del nums[5]

# ----------- Average of the numbers entered by the users ------------

num_list = [];

# while True:
#     inp = input("Enter a number: ");
#     if inp == 'done':
#         break;
#     value = float(inp);
#     num_list.append(value);
    
# print(num_list)
# average = sum(num_list)/len(num_list);
# print("Average:", average)

# -------- Create new list from 2 lists, odd-index element from first list and even-index element from second list
list_one = [4,12,16,21,24,28,32]
list_two = [5,10,15,20,25,30,35]
list_three = []
list_three = list_one[1::2] + list_two[0::2];

# for i in range(0,len(list_one)):
#    if i % 2 != 0:
#        list_three.append(list_one[i]);

# for i in range(0,len(list_two)):
#     if i % 2 == 0:
#         list_three.append(list_two[i]);

print(list_three)

# ------------ THree Equal Chunks -------------
sample_list = [21,55,18,33,24,22,68,35,79]
# chunk_1 = sample_list[0:3]
# chunk_2 = sample_list[3:6]
# chunk_3 = sample_list[6:9]

# chunk_1.reverse()
# chunk_2.reverse()
# chunk_3.reverse()

# print("Chunk-1:", chunk_1)
# print("Chunk-2:", chunk_2)
# print("Chunk-3:", chunk_3)


# With loop
length = len(sample_list)
chunk_size = int(length/3)
num_of_chunks = length//chunk_size

# NB: PAGINATION FORMULA

# print(length, chunk_size, num_of_chunks)
# print(sample_list)
# for index in range(0,num_of_chunks):
#         # Step has to increase by chunk size to start from the end of previous chunk
#         chunk = sample_list[index * chunk_size:chunk_size * (index+1)]
#         chunk.reverse()
#         print(f"Chunk-{index + 1}: {chunk}");

# Or

start = 0;
end = chunk_size;

for index in range(0,num_of_chunks):
    chunk = sample_list[start:end]
    chunk.reverse()
    print(f"Chunk-{index + 1}: {chunk}");
    # Start is the end of the previous chunk
    start = end;
    # end is the end of the current chunk + chunk size
    end = end + chunk_size;
    
    
    
    
    
    
# *************** LISTS AND STRING: COnvert Strings to a list and vice versa ***************
# 1) Convert String to List
custom_String = "Hello"
custom_String = list(custom_String);
print(custom_String) # ['H', 'e', 'l', 'l', 'o']

# Back to String
new_string = ''.join(custom_String)
print(new_string) # Hello

# Split MEthod
string_2 = "hello world. I love python programming"
split_string = string_2.split(' ')
print(split_string) # ['hello', 'world.', 'I', 'love', 'python', 'programming']

# Join with Join again
new_string = ' '.join(split_string)
print(new_string) # hello world. I love python programming

nums = [1,2,3,4,5]
# Join cannot work on integers, so we convrt them to string
for item in nums:
    nums[nums.index(item)] = str(item)
    
nums_join = ' | '.join(nums)
print(nums_join) # 1 | 2 | 3 | 4 | 5