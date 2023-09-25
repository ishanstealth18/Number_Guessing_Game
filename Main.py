import random

lower_bound_val = int(input("Enter lower bound value : "))
upper_bound_val = int(input("Enter upper bound value : "))

num_to_be_guessed = random.randint(lower_bound_val, upper_bound_val)
#print("Number to be guessed is: ", num_to_be_guessed)

print("You have only 7 chances to guess the correct number!!")

turn = 1
count = 0
while turn < 8:
    if count == 7:
        print("Sorry, you lost, please try again!!")
        break
    count += 1
    input_num = int(input("Guess a number: "))
    num_difference = num_to_be_guessed - input_num
    if input_num == num_to_be_guessed:
        print("Congratulation, you did it in {} try.".format(count))
        break
    elif input_num != num_to_be_guessed:
        if num_difference < 0:
            num_difference = -num_difference
            if num_difference <= 10:
                print("Input number is a bit high!!")
            elif 10 < num_difference <= upper_bound_val:
                print("Input number is very high!!")
        else:
            if num_difference <= 10:
                print("Input number is a bit low!!")
            elif 10 < num_difference <= upper_bound_val:
                print("Input number is very low!!")







