## PCEP Training Module 2.2

## Octal and Hex conversion built into print()
print(0o123) ## Octal with prefix 0o (Zero and lower case o)
print(0x123) ## Hex with prefix 0x (Zero and lower case x)

## Scientific notation is also built in to print()
print(3e8) ## E or e can be used as x10 and the following number gives the power NOTE the answer will be a float
print(0.0000000000000000000001) ## Will output in scientific notation

## Escape character
print("I like \"Monty Python\"") ## Will print the same as below
print('I like "Monty Python"') ## Will print the same as above

## Printing booleans
print(True > False) ## Will print "True" noting that True is "greater than" False
print(True < False) ## Will print "False" noting that True is "less than" False

## Challenge 1
## Print the following output
## "I'm"
## ""Learning""
## """Python"""
print("\"I\'m\"\n\"\"Learning\"\"\n\"\"\"Python\"\"\"")