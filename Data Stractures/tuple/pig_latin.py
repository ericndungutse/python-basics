message = input("Enter English message to translate into Pig Latin: ");
message_list = message.split();
pig_latin = [];

vowels = 'aeiouAEIOU'
for word in message_list:
    from_position = 0;
    suffix = ""
    prefix= "";
    if word[0].isalpha():
        for char in word:
            if char not in vowels:
                suffix += char
                from_position += 1;
                prefix = 'ay'
            else:
                prefix = 'yay';
                break;
        pig_latin.append(word[from_position:] + suffix + prefix);
    elif word[0].isdigit():
        # remove digits from the word
        prefix_digits = ""
        word_string = ""
        for char in word:
            if char.isdigit():
                prefix_digits += char;
            else:
                if(not prefix_digits.__contains__("-")):
                    prefix_digits += "-";
                word_string += char;
        
        # Convert to pig latin
        from_position = 0;
        suffix = ""
        for char in word_string:
            if char not in vowels:
                suffix += char
                from_position += 1;
            else:
                break;
            
        # Add to pig latin list
        digit_lists = prefix_digits.split("-");
        lating_word = word_string[from_position:] + suffix + "ay";
        final_pig_latin = digit_lists[0] + lating_word + digit_lists[1];
        pig_latin.append(final_pig_latin);
           
                

print("Pig Latin:", ' '.join(pig_latin));

