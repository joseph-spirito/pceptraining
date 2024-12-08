## PCEP Training Module 2.6
## PCEP Module 2.5 was over commenting code

## Input can't be controlled as only strings or other value types. Do NOT store them with an operation
## EXAMPLE
## anything = input("Enter a number: ")
## something = anything ** 2.0     SUPER WRONG
## print(anything, "to the power of 2 is", something)  WILL MOST LIKELY RESULT IN A TYPE ERROR

## We can wrap an input() with a float(input())
## Still risk a char or string entered

## Simple example with perfect client in mind
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5 ## Sqroot(a^2 + b^2)
print("Hypotenuse length is", hypo)

## Example of concatination between two string input variables
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

## Fancy example of multiplying strings by making a box in the terminal
print("+" + 10 * "-" + "+") ## Returns "+" 10x"-" "+"
print(("|" + " " * 10 + "|\n") * 5, end="") ## Returns parallel lines 5 times
print("+" + 10 * "-" + "+") ## Returns a copy of the first line

## We can convert data types to strings easily
## str(number) where "number" is an int or float variable

## Challenge
a = float(input("Enter a number: "))# input a float value for variable a here
b = float(input("Enter another number other than zero: "))# input a float value for variable b here

print(a + b)# output the result of addition here
print(a - b)# output the result of subtraction here
print(a * b)# output the result of multiplication here
print(a / c)# output the result of division here

print("\nThat's all, folks!")

## Challenge
x = float(input("Enter value for x: ")) ## Recieve input of an int or float

y = 1 / (x + 1 / (x + 1 / (x + 1 / x))) ## calculate for f(x) = 1 / x + 1 / x + 1 / x + 1 / x

print("y =", y) ## Return y = f(x)

## Challenge
## User enters start time of a trip in variabls "hour" and "min"
## User enters duration time in minute incriment
## Display what the time will be at the end of the trip (24 hour clock and time zones aren't real)
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

final_hours = dura // 60 ## Calculate hours of trip
final_min = (dura % 60) + mins ## Gather minutes of trip after hours are excluded and add to start minutes
final_hours += final_min // 60 ## Check if minutes added to original time will make another hour
final_hours += hour ## Consolidate hours
final_hours %= 24 ## Calculate end hours for 24 hour flip
final_min %= 60 ## Rinse final minute time

print("End time will be:", str(final_hours) + ":" + str(final_min))  ## Display end-of-trip time
## To be honest, I know there is a better way to write this even in the scope. I did it quick and dirty