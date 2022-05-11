user_input = input("What roman figure do you want to change to numerals?\n:")
unique_characters = {
    "i": 1,
    "v": 5,
    "x": 10,
    "l": 50,
    "c": 100,
    "d": 500,
    "m": 1000
}
n = len(user_input)
value = unique_characters[user_input[-1]]
for character in range(n-2, -1, -1):
    current_letter = user_input[character]
    after_letter = user_input[character + 1]
    if unique_characters[current_letter] >= unique_characters[after_letter]:
        value += unique_characters[current_letter]
    else:
        value -= unique_characters[current_letter]
print(value)

