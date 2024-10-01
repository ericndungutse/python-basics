def sentence_maker(text):
    question_words = ["what",  "how", 'where']
    capitalized_text = text.capitalize()
    for word in question_words:
        if text.startswith(word):
            # return f"{capitalized_text}?"
            return "{}?".format(capitalized_text)
        return "{}.".format(capitalized_text)

result = [];

while True:
    user_input = input("What is in your? ")
    if user_input == "\end":
        break
    else:
        result.append(user_input)

print(result)