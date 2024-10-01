import random

word_list = ['UDEMY', "APPMILLERS", "PYTHON"]

secret_word = random.choice(word_list);
length_word = len(secret_word);

print(secret_word);

blanks = [];
guessed_letters = [];


# _ means the element is not needed
for _ in range(length_word):
    blanks.append("_");
    
print(" ".join(blanks))
lives = 6

end_game = False
while not end_game:
    if lives == 0:
        end_game = True;
        print('Game over! You lost')
    
    guess = input("Guess a letter: ").upper();
    
    if guess not in secret_word:
        print("Wrong latter")
        lives -= 1;
        continue;
    

    if guess in guessed_letters:
        print("You already guessed that letter");
        continue;
    
    else:
        guessed_letters.append(guess);


    for position in range(length_word):
        letter = secret_word[position];
        if letter == guess:
            blanks[position] = guess;
    
    if "_" not in blanks:
        end_game = True;
        print("You win!");
    if end_game:
        ask = input("Do you want to play again? (Y/N)")
        if ask == 'Y':
            secret_word = random.choice(word_list)
            blanks.clear();
            length_word = len(secret_word)
            for _ in range(length_word):
                blanks.append("_")
            guessed_letters.clear();
            lives=6
            end_game = False;
        else:
            print("See you next time")
            
        
    print(" ".join(blanks));
        
