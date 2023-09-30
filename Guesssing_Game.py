import  random


name = input("Enter your name: ")
print("Good Luck! {}".format(name))

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Function will choose one random
# word from this list of words
word = str(random.choice(words))

word_to_update = ""

for letter in word:
    word_to_update = word_to_update + "-"

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
