import random

print("Winning Rules of the Rock paper and scissor game as follows:\nrock vs paper->paper wins\n"
      "rock vs scissors->rock wins\npaper vs scissors->scissors wins")

print("Enter Choice:\n1. Rock\n2. paper\n3. scissor")

player_1 = 'User'
player_2 = 'Computer'


# Function to choose option for human player
def choose_option(input_num, player_name):
    if input_num == 1:
        print("{} choice is: Rock".format(player_name))
    elif input_num == 2:
        print("{} choice is: Paper".format(player_name))
    else:
        print("{} choice is: Scissor".format(player_name))


# Function to choose random option for computer
def play_computer_turn():
    random_num = random.randint(1, 3)
    # print("Computer random number: {}".format(random_num))
    return random_num


# Function to compare values for user selection and computer selection
def compare_result(user_option, computer_option):
    if user_option == 1 and computer_option == 1:
        print("Draw")
    elif user_option == 1 and computer_option == 2:
        print("Rock v/s Paper\nPaper wins=>Computer wins")
    elif user_option == 1 and computer_option == 3:
        print("Rock v/s Scissor\nRock wins=>User wins")
    elif user_option == 2 and computer_option == 2:
        print("Draw")
    elif user_option == 2 and computer_option == 3:
        print("Paper v/s Scissor\nScissor wins=>Computer wins")
    elif user_option == 2 and computer_option == 1:
        print("Paper v/s Rock\nRock wins=>User wins")
    elif user_option == 3 and computer_option == 3:
        print("Draw")
    elif user_option == 3 and computer_option == 1:
        print("Scissor v/s Rock\nRock wins=>Computer wins")
    else:
        print("Scissor v/s Paper\nScissor wins=>User wins")


# Logic to keep playing game till user wants.
while True:
    user_choice = int(input("User turn: "))
    choose_option(user_choice, player_1)

    computer_choice = play_computer_turn()
    choose_option(computer_choice, player_2)

    compare_result(user_choice, computer_choice)

    another_game = input("Do you want to play another game? (Y/N)")
    if another_game == 'Y':
        continue
    else:
        print("Thank you for playing, see you next time!!")
        break
