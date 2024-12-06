## PCEP Training Module 2.1

## use the "print()" function to print the line "Hello, Python!" to the screen. Use Double quotes around the string;
print("Hello, Python!")

## having done that, use the "print()" function again, but this time print your first name;
print("Joseph")

## remove the double quotes and run your code. Watch Python's reaction. What kind of error is thrown?
## print(Joseph)  * THROWS NameError: name 'Joseph' is not defined *

## then, remove the parentheses, put back the double quotes, and run your code again. Whit kind of error is thrown this time?
## print Joseph * THROWS SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)? *

## experiment as much as you can. Change double quotes to single quotes, use multiple "print()" functions on the same line, and thenon different lines. See what happens.
print('Single quote test') ## works just fine
## print("Single ") print("line ") print("test ") * THROWS SyntaxError: invalid syntax *
print(123) ## Integer test, works just fine
print() ## Empty test, works just fine
print(1.2) ## Float test, works just fine
print("\n\"\\n\" test") ## works just fine
print("Multiple", "argument", "test") ## works just fine, NOTE spaces are NOT required between arguments

## Keyword arguments

## end
print("End test to conjoint", end=" ") ## interesting. never knew this existed. default is end="\n"
print("seperate line print functions") ## end="" will result in same result as end=" "

## sep
print("Sep", "test", 1, 2, 3, sep="-") ## works with integers as well

## CHALLENGE 1 ##
## make 
## print("Programming", "Essentials", "in")
## print("Python")
## say Programming***Essentials***in...Python

print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")
