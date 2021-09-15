# -*- coding: utf-8 -*-
"""

Edmond Tongyou
CPSC 223P-01
Tues March 9 14:47:33 2021
tongyouedmond@fullerton.edu

"""

# Importing random for randint()
import random

computerScore = 0
ties = 0
userScore = 0

computerChoice = ""
userChoice = ""

# Loops until the exit condition (Q) is met otherwise keeps asking for
# one of three options (R, P, S), every loop the computer choice is
# decided via randint and then compares the user choice to the
# computer choice. If user wins, adds 1 to userScore same with computer
# win. If a tie is found adds 1 to the ties. If the inputted letter is
# not R P S or Q then the loop repeats until a valid option is inputted
while 'Q' not in userChoice:
    computerChoice = random.randint(0, 2)
    print ("Please input one: (R, P, S, Q) > ", end = " ")
    userChoice = input()
    userChoice = userChoice.upper()

    if 'R' in userChoice  or 'P' in userChoice or 'S' in userChoice:

        if computerChoice == 0:
            print("Computer chose Rock", end = '. ')
            if 'R' in userChoice:
                print("Call it a draw.")
                ties += 1
            elif 'P' in userChoice:
                print("You win.")
                userScore += 1
            else:
                print("Computer wins.")
                computerScore += 1
        elif computerChoice == 1:
            print("Computer chose Paper", end = '. ')
            if 'R' in userChoice:
                print("Computer wins.")
                computerScore += 1
            elif 'P' in userChoice:
                print("Call it a draw.")
                ties += 1
            else:
                print("You win.")
                userScore += 1
        else:
            print("Computer chose Scissors", end = '. ')
            if 'R' in userChoice:
                print("You win.")
                userScore += 1
            elif 'P' in userChoice:
                print("Computer wins.")
                computerScore += 1
            else:
                print("Call it a draw.")
                ties += 1
    elif 'Q' in userChoice:
        continue
    else:
        print("Invalid option, input again.")
        continue

# Prints out the results for each score then compares the scores to see who won
# or if a tie was found.
print("Computer: " , computerScore)
print("You: ", userScore)
print("Ties: ", ties)

if computerScore > userScore:
    print("Computer Won!")
elif computerScore < userScore:
    print("You Won!")
else:
    print("It's a tie!")