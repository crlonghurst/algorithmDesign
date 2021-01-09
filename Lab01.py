# 1. Name: 
#    Christian Longhurst
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    This program is to demonstrate a simple guess the number game, where you enter the parameter of how large of an area. Then the program
#    determines a random number within the parameters of 0 and what the user enters. After the program decides on the random
#    integer the user can guess with the program telling the user if they are to high or to low.
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part of this program was getting a grasp on python. I have rarely used python, so it took me a while to 
#    stop using brackets and paranthesis. The actual design of how to complete the assignment was pretty straightforward since I
#    have done programming for a while in other languages so actually having the idea of how to accomplish what was needed was in my
#    toolset just not this specific language.
# 5. How long did it take for you to complete the assignment?
#    It took me about an hour to complete this program from start to turning it in.

import random
import array as arr

# Game introduction
print("This is the \"guess a number\" game.")
print("You try to guess a random number in the smallest number of attempts.")


# Prompt the user for how difficult the game will be. Ask for an integer
string_max = input("Pick a positive integer:\n")

value_max = int(string_max)
# Generate a random number between 1 and the chosen value
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing


# Initialize the sentinal and the array of guesses
turnCount = 0
guesses = []
guess = 0
# Play the guessing game
while guess != value_random:
    
    # Prompt the user for a number
    guess = int(input(">"))

    # Store the number in an array so it can be displayed later
    guesses.append(guess)
    turnCount += 1
    # Make a decision: was the guess too high, too low, or just right
    if guess > value_random:
        print("\tToo High!!! Try again!")
    elif guess < value_random:
        print("\tToo Low!!! Try Again!")
    elif guess == value_random:
        break

guessAmount = str(turnCount)
print("You were able to find the number in "+guessAmount+" guesses")
print("The numbers you guessed were: [",end="")
for x in guesses:
    if x == value_random:
        print(str(x), end="")
    else:
        print(str(x)+", ", end="")

print("]")
# Give the user a report: How many guesses and what the guesses where
