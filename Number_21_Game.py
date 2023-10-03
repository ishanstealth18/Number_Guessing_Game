import random

num_count = 0
num_lst_generated = []
computer_no_lst = []
computer_turn = False
user_turn = False


# This function will create random number for the user and add it to the list
def generate_random_nos(num_lst, quantity, last_no):
    for i in range(0, quantity):
        last_no += 1
        num_lst.append(last_no)
    return num_lst


# This function will check if the threshold value is crossed or not after every turn
def check_threshold(user_lst_num, computer_lst_num, user_last_turn, computer_last_turn):
    # print("User last turn: {}, Computer last turn: {}".format(user_last_turn, computer_last_turn))
    if not user_lst_num or not computer_lst_num:
        return
    else:
        # print("User last number: {}, computer last number: {}".format(user_lst_num, computer_lst_num))
        if user_lst_num[-1] >= 21 and user_last_turn == True:
            print("Sorry, you lost, computer win!!")
            return True
        elif computer_lst_num[-1] >= 21 and computer_last_turn == True:
            print("Congratulations!!, you win!!")
            return True
        else:
            return


# This function will generate random number for computer's turn and add it to the list
def play_computer_turn(num_lst, no_count):
    # print("Last number for computer: ", no_count)
    generate_count = random.randint(1, 9)
    # print("Random number count for computer: ", generate_count)
    for no in range(0, generate_count):
        no_count += 1
        num_lst.append(no_count)
    return num_lst


print("Player 2 is computer.")
ask_to_play = input("Do you want to start the game? (Yes/No)")

# Logic to ask if user wants to play this game or not
if ask_to_play == "Yes":
    turn_type = input("Enter 'F' to take the first chance.\nEnter 'S' to take the second chance : ")
    # Logic to check if player wants to play first or second
    if turn_type == 'F':
        # Logic to play the game till value 21 is reached
        while True:
            if num_lst_generated is None:
                num_count = 0

            number_quantity = int(input("How many number you wish to enter: "))
            num_lst_generated = generate_random_nos(num_lst_generated, number_quantity, num_count)
            print("Order of input after your chance: ", num_lst_generated)
            num_count = num_lst_generated[-1]
            user_turn = True
            computer_turn = False

            if check_threshold(num_lst_generated, computer_no_lst, user_turn, computer_turn):
                break

            computer_no_lst = play_computer_turn(num_lst_generated, num_count)
            print("Order of input after computer turn: ", computer_no_lst)
            num_count = computer_no_lst[-1]
            user_turn = False
            computer_turn = True

            if check_threshold(num_lst_generated, computer_no_lst, user_turn, computer_turn):
                break

    else:
        while True:
            user_turn = False
            computer_turn = False
            if num_lst_generated is None:
                num_count = 0

            # print("Current num list: ", num_lst_generated)
            computer_no_lst = play_computer_turn(num_lst_generated, num_count)
            print("Order of input after computer turn: ", computer_no_lst)
            num_count = computer_no_lst[-1]
            user_turn = False
            computer_turn = True

            if check_threshold(num_lst_generated, computer_no_lst, user_turn, computer_turn):
                break

            number_quantity = int(input("How many number you wish to enter: "))
            num_lst_generated = generate_random_nos(num_lst_generated, number_quantity, num_count)
            print("Order of input after your chance: ", num_lst_generated)
            num_count = num_lst_generated[-1]
            user_turn = True
            computer_turn = False

            if check_threshold(num_lst_generated, computer_no_lst, user_turn, computer_turn):
                break

else:
    print("Thank you for your time!!")
