import random;

# Step 1: Get 5 random unique numbers between 1 and 69
def read_inputs():
    print("Enter 5 different number between 1 and 69 with spaces between them.")
    response = input('> ');
    numbers = response.split(' ');
    return numbers

def convert_to_integers(numbers_list):
    numbers = [];
    for i in range(0, 5):
        numbers[i] = int(numbers_list[i]);
    return numbers;

def check_if_inputs_are_five(numbers_list):
    if len(numbers_list) != 5:
        return False;
    return True;

while True:
    # Read Numbers
    inputs = read_inputs();
    
    # Check if inputs are five
    isFive = check_if_inputs_are_five(inputs);
    
    # Restart if inputs are not five
    if(not isFive):
        print("🔥 Error: You must enter 5 numbers");
        continue;
    
    # Convert To numbers
    numbers_list =[]
    try:
        for i in range(5):
            num = int(inputs[i]);
            numbers_list.append(num);
    except ValueError:
        print("🔥 Error: You entered non integer values");
        continue;
    
    # check if integers/numbers are in range: >=1 and <=69
    isInRange = True;
    for item in numbers_list:
        if not(1<=item<=69):
            print("🔥 Error: You must enter numbers between 1 and 69");
            isInRange = False;
            break;
    if not isInRange:
        continue;
    
    # Check if numbers are unique
    if len(set(numbers_list)) != 5:
        print("🔥 Error: You must enter 5 unique numbers");
        continue;
    
    break

# Step 2: GetPowerball from 1 to 26
def read_powerball():
    while True:
        try:
            print("Enter Powerball between 1 and 26");
            response = input('> ');
            response = int(response);
            if not(1<=response<=26):
                raise Exception("🔥 Error: You must enter a number between 1 and 26");
            return response
        except ValueError:
            print("🔥 Error: You must enter a number");
            continue;
        except Exception:
            print("🔥 Error: You must enter a number between 1 and 26");
            continue;
        
# Step 3: Attempts
def read_attepts_times():
    while True:
        try:
            print("Enter number of attempts (Max: 1000000)");
            response = input('> ');
            response = int(response);
            if not(1<=response<=1000000):
                raise Exception("🔥 Error: You must enter a number between 1 and 1000000");
            return response
        except ValueError:
            print("🔥 Error: You must enter a number");
            continue;
        except Exception:
            print("🔥 Error: You must enter a number between 1 and 1000000");
            continue;

# Step 4: Run Game
powerball = read_powerball();
number_of_attempts = read_attepts_times();
print(f"It costs ${number_of_attempts * 10} to play {number_of_attempts} times.")

input("Press enter to start...")

# Generate possible numbers: 1 - 69
possibleNumbers = list(range(1, 70));
for i in range(0, number_of_attempts +1):

    # Generate random lottery numbers from the possible numbers.
    lotteryNumbers = random.sample(possibleNumbers, 5);

    # Generate Powerball number
    winningPowerball = random.randint(1, 26);
    print("The winning numbers are: ", end="")
    
    winning_numbers = ''
    for num in lotteryNumbers:
        winning_numbers += f"{num} "
    winning_numbers += f"and {winningPowerball}"
    
    # Determine if player won: Use sets to compare
    playerNumbers = set(numbers_list);
    winningNumbers = set(lotteryNumbers);
    won = (playerNumbers == winningNumbers) and winningPowerball == powerball;
    if won:
        winning_numbers = winning_numbers + " You won! 🎉";
        break;
    else:
        winning_numbers = winning_numbers + " You lost! 😢";
    print(winning_numbers)


     