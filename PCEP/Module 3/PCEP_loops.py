## PCEP Training Module 3.2

## While loops

## Basic look of while loop
## while x > 20:
##      instruction

## Basic infinite loop
## while True:
##      print("Baby Shark")

## Challenge
## Finishing a game where the user guesses a number
## If the number guessed is wrong, keep them guessing in a loop
## If the number guessed is correct, congratulate and exit loop

## Given Code NOTE tripple quotes can let you enter more than one line at a time
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

## Write code here
user_guess = int(input()) ## User inputs any number

while user_guess != secret_number:
    print("Ha ha! You're stuck in my loop!") ## Antagonize the user
    user_guess = int(input()) ## Wait for input

print("Well done, muggle! You are free now.") ## Backhanded comment

## For loops

## Basic example
## for i in range(100):     ## "i" will start at 0 unless designated otherwise and stop at 99
##      # do_something

## Another spin
## for i in range(2, 8):    ## "i" will start at 2 and end at 7
##      # do_something

## Three arguments
## for i in range(2, 8, 3)  ## "i" will start at 2, end at 7, and increment by 3
##      #do_something

## "i" can be interchanged with any variable name
## Example given
power = 1 ## I do think this is an odd variable name. It should be "result" in the given code example
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

