import random

name = input("Enter your name: ")
print("Good Luck! {}".format(name))

# List of words
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Function will choose one random
# word from this list of words
word = str(random.choice(words))

word_to_update = ""

# Create another variable to store the word
for letter in word:
    word_to_update = word_to_update + "-"

'''
Check for the input letter and compare with each letter in the word and then
replace '-' with alphabet.
Once all the letters are replaced, declare the winner.
'''

while True:
    if "-" not in word_to_update:
        print("You Win!!")
        print("The word is : {}".format(word))
        break
    print(word_to_update)
    input_letter = input("Guess the character: ")
    for i in range(len(word)):
        if input_letter == word[i]:
            get_index = i
            word_to_update = list(word_to_update)
            word_to_update[get_index] = input_letter
            word_to_update = "".join(word_to_update)
