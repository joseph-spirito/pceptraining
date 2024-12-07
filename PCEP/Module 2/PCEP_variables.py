## PCEP Training Module 2.4

## Variable convention is lower-case with _ sep OR camalCase
## To declair a variable, just make a name and assign a value.

numbuh = 1
account_balance = 1000.0
client_name = 'John Doe'
print(numbuh, account_balance, client_name)

## Variables can be appended on the end of strings
python_version = "3.11.5"
print("Python version: " + python_version) ## NOTE using the "+" symbol to append instead of "," to build a string will not auto push a space between appending values

## Values can be overwritten in variables
sample_var_1 = 1
print(sample_var_1) ## Returns value "1"
sample_var_1 = sample_var_1 + 1
print(sample_var_1) ## Returns value "2"

## Values can be overwritten without manipulation of original data

sample_var_2 = 100
sample_var_2 = 200 + 300
print(sample_var_2) ## Returns value "500"

## Data can be stored by referensing other variables
a = 3.0
b = 4.0
c = (a ** 2 + b **2) ** 0.5 ## Sqroot = ^1/2
print("c =", c)

## Challenge
## John has three apples
## Mary has five apples
## Adam has six apples
## Store the values in variables assigned to each name
## Store the total number of apples in a variable named "total_apples"
## Print "Total number of apples:" with the total number of apples
john = 3
mary = 5
adam = 6
total_apples = john + mary + adam
print("Total number of apples:", total_apples)

## Data manipulation has shorthand with operations
sheep = 1
print("Number of sheep:", sheep) ## Returns "Number of sheep: 1"
sheep += 1 ## same as "sheep = sheep + 1"
print("Number of sheep:", sheep) ## Returns "Number of sheep: 2"

## This manipulation can be done in a more elaborate form
sample_var_3 = 3
sample_var_3 += 2 * 3 ## same as "sample_var_3 = sample_var_3 + 2 * 3"
print(sample_var_3) ## Returns 9 NOTE Order of operations is still followed

## Challenge
## Conversion between miles and kilometers
## Given variables
kilometers = 12.25
miles = 7.38

## Code insertion
miles_to_kilometers = miles * 1.61 ## Originally commented out
kilometers_to_miles = (1 / 1.61) * kilometers ## Originally commented out

## Given output formulas
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

## Challenge
## Evaluate y = 3x^3-2x^2+3x-1
## Given code
x = 0
x = float(x)

## Code insertion
y = 3 * (x ** 3) - 2 * (x ** 2) + 3 * x - 1 ## Remember order of operations for exponents is different in Python

## Given code
print("y =" , y) ## With given value of x = 0, return is "-1.0"