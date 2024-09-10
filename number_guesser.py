import random 

#gets an integer from the user, forcing numbers only 
def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Only number guesses: ")


'''
This allows the user to make a guess
a num variable is used as a counter to determine 
how many tries it takes the user to guess the problem

'''
def guess():

    num = 1 

    while True:
        

        user_guess = get_int(f"guess {num}: ")

        print("")

        if user_guess == game_answer:
            print("Hey you got the correct number\n")
            print(f"You got it within {num} trys\n")
            break
        
        num += 1





def main():

    print("Welcome to the number guesser! \n")

    while True:

        lower_range = get_int("What would you like the lower limit of the guessing to be: \n")
        higher_range = get_int("What would you like the higher limit of the guessing to be: \n")

        print("")

        if lower_range < higher_range:
            break
        else:
            lower_range = get_int("What would you like the lower limit of the guessing to be: \n")
            higher_range = get_int("What would you like the higher limit of the guessing to be: \n")


    global game_answer
    game_answer = random.randint(lower_range, higher_range)
    

    print("Begin guessing\n")

    guess()


main()