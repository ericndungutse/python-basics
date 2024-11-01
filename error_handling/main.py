
def square(num):
    try:
        sq = num * num
        print("Product id:",num*num);
        dict = {1: "One", 2:"Two"}
        print("The value is: ", dict[num]);
    except TypeError as message:
        print("ERROR:", message);
    except KeyError as msg:
        print(f"ERROR: {msg} key not found");
    else:
        print(f"sq is {sq * sq}");
    finally:
        print("Finally block executed");

# number = int(input("Enter a number: "));
# square(number)

# RAISING EXCEPTIONS
number = int(input("Enter a number: "));
if number < 0:
    raise ValueError("Number cannot be negative");