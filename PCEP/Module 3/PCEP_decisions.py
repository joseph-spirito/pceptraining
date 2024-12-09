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

