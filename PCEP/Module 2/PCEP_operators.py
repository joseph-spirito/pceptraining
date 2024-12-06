## PCEP Training Module 2.3

## Operations can be done in the print()
print(2+2)

## ** is an exponential operator. Before the "**" is the base, after is the exponent
print(2**3) ## The console prints 8

## If one number is specified as a float, then the answer will be returned as a float. The return will be a float if both numbers are a float as well.
print(2**3.) ## Console will show a result of 8.0

## A singular "*" will be the multiplication. Results of floats follow the same rules.
print(2*3) ## Returned value of 6
print(2*3.) ## Returned value of 6.0

## / is used for division. NOTE Results of a division is ALWAYS a float type.
print(6/3) ## Returned value of 2.0
print(6./3) ## Returned value of 2.0

## // is integer divisional. This operation follows the original float rules. NOTE The answer will be rounded DOWN
print(6//3) ## Returned value of 2
print(6.//3) ## Returned value of 2.0
print(6//4) ## Returned value of 1
print(6//4.) ## Returned value of 1.0 instead of 1.5
print(-6.//4) ## Returned value of -2.0 insead of -1.5

## % is to calculate the remainder of division "modulo" NOTE Follows float rules
print(14%4) ## 4 goes into 14 a total of 3 times with a remainder of 2. Returned value of 2
print(12%4.5) ## Returned value of 3.0

## Addition "+" and subtraction "-" perform as expected and also follow float rules
print(4+3-1) ## Returned value of 6
print(4+3-1.) ## Returned value of 6.0

## Equations read left to right EXCEPT for exponential equations
print(2*2*3) ## 2*2=4, 4*3=12, Returned value of 12
print(2**2**3) ## 2^3=8, 2^8=256, Returned value of 256