## PCEP Training Module 3.1

## Booleans

## "==" is a comparative statement to see if both sides are the same
## "!=" is a comparative statement to see if both sides are not equal

## 2 == 2 Will return True
## 2 == 2. Will return True, Python can convert an intever into its real equivalent
## 1 == 2 Will return False

## Example "=="
var = 0  # Assigning 0 to var
print(var == 0) ## Returns True

var = 1  # Assigning 1 to var
print(var == 0) ## Returns False

## Example "!="
var = 0  # Assigning 0 to var
print(var != 0) ## Returns False

var = 1  # Assigning 1 to var
print(var != 0) ## Returns True

## "<", ">", "<=", and ">=" comparators
## Works just like math class

## Challenge
## No "if" statement, and only two lines of code
## User inputs an integer
## If input is less than 100, print False
## If input is greater than or eaqual to 100, print True

n = int(input("Give me an integer: "))
print(n >= 100)

## IF STATEMENTS!!!

## Basics, state "if", find a binary to go against, nest an action
## if true_or_not:
##  do_this_if_true

## ELSE STATEMENTS!!!

## if ture_or_false_condition:
##  perform_if_condition_true
## else:
##  perform_if_condition_false

## Nesting statements

## if the_weather_is_good:
##     if nice_restaurant_is_found:
##         have_lunch()
##     else:
##         eat_a_sandwich()
## else:
##     if tickets_are_available:
##         go_to_the_theater()
##     else:
##         go_shopping()

## ELIF

## if the_weather_is_good:
##     go_for_a_walk()
## elif tickets_are_available:
##     go_to_the_theater()
## elif table_is_available:
##     go_for_lunch()
## else:
##     play_chess_at_home()

## Challenge
## Citizens making more than 85,258 "thalers", they are taxed 32% the surplus over the threshold PLUS 14,839.02 flat
## Citizens making the threshold or less are taxed 18% minus 556.02

## Given code
income = float(input("Enter the annual income: "))

## Write code here
tax = 0.0
if income <= 85258.0:
    tax = (income * 0.18) - 556.02
else:
    tax = ((income - 85258.0) * 0.32) + 14839.02

## Given code
tax = round (tax, 0)
print("The tax is:", tax, "thallers")

## Challenge
## Leap year identifier
## if the year number isn't divisible by four, it's a common year
## otherwise, if the year number isn't divisible by 100, it's a leap year
## otherwise, if the year number isn't divisible by 400, it's a common year
## otherwise, it's a leap year
## NOTE Leap years did not start until 1582

## Given code
year = int(input("Enter a year: "))

## Write code here
type_of_year = ""

if year < 1582:
    type_of_year = "Not within the gregorian calendar period"
elif (year % 4) != 0:
    type_of_year = "Common year"
elif (year % 100) != 0:
    type_of_year = "Leap year"
elif (year % 400) != 0:
    type_of_year = "Common year"
else:
    type_of_year = "Leap year"

print(type_of_year)