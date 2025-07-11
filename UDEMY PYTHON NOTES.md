UDEMY PYTHON NOTES

-python is dynamically typed (at runtime)
-this means one variable can be assigned and reassigned to values of different types
-don't need a semicolon to end lines
-indentation for function / code hierarchy

COMMENTING
-single line comments:
    #can leave single line comments like this

-multi line comments written like the following are actually strings:
"""muti-line comments are written in triple quotes
like this. We can use single or double triple quotes."""

MATH
- // Floor division , aka division no remainder
- ** Exponentiation
- % Modulo () , aka return the remainder of x / y 
- round(float, # of digits to round to), returns a float
- for console operations : _ is equal to the last calculated value (just for math/ numeric?)
- can interchange ints, floats (multiple number types) in equations
- type casting / conversions => area = 78.5, int(area) = 78
- support for +=, but no ++ increment

STRINGS
-python supports unicode out of the box (emojis / other languages in strings)
-double and single quote strings supported
-comments:
    - "# can leave single line comments like this"
    -can also write multi line comments written with triple quotes, but its actually just a string
    """muti-line comments are written in triple quotes
    like this. We can use single or double triple quotes."""
-escapes in python (i.e if u wanna use single quotes in a string, use double quotes outside the string)
-backslash before characters that would end the string to embed the char in string
-"\n" is the newline 
-concatenation : 
--- NOTE: THIS IS OLDER (STILL VALID) BUT MORE VERBOSE ---
    - string concat achieved w + sign ex : print (string + string2)
    -to print a string multiple times -> print (3 * hello) == hellohellohello
    -to include variables in a string : {} as a placeholder w/in the string, .format(varName)
        -ex. print("My name is {}".format(name))
        -can embed multiple vars in order
-The current best practice for string concatenation: 
    -use F-strings aka f"string {variable1} string continues {variable2}"
    -this method is more readable/performant
-string methods/functions
    - .upper() -> to uppercase
    - .lower() -> to lowercase
    - len(string) -> string length
    - string.replace(x, y) -> replace all instances of x with y (match capitalization etc.)
    -split => split a long string into list of strings (by default splits at spaces)
    -not technically char objects, just strings of length 1
    -to access the chars, use array access (ex. string[1],
    can also do a range such as string[0:5] (gets string from index 0 to 5))
    -can use negative numbers to get the last char, 2nd from last etc.
        -i.e to print the last 38 char of string, string[-38:]
    
IF/ELSE STATEMENTS
-dont use curly braces / etc, rather show hierarchy / blocks with indentation 
-technically, single space / double space etc. will work, but best practice is 4 spaces or a tab
-if, else, elif
- == is checking for exact equality, != not equal
-can ask if things are between / within a range
- and (logical and keyword)
- "if var:" checks if var has a value that is nonzero / not NONE

USER INPUT
-input() -> this function takes user input
-to also send a message to user, and save user input:
    -student_name = input("Enter student name: ")
-user input is by default consumed / saved as a string
-if you want to take user input as a number or some other type, must explicitly type cast

FUNCTIONS
-declare with def
-parameters, can set default value ex. name="maddy", age=2
-return values w return keyword
-dont HAVE to return something
-type checking example below:
'''
def printtype(val):
    valtype = type(val)
    if valtype == int:
        return "Int"
    elif valtype == float:
        return "Float"
    else:
        return "String"
'''

LISTS, TUPLES, SETS
-Python lists are arrays
-can include values of different types 
-can insert into list -> list.insert(index, value)
-delete items with del(list[index]) (index based)
-list.remove(value) (value based)
-len = length
-tuples: immutable list, instead of square brackets, use parentheses, can cast with tuple() or list()
-sets : unique set (no repeat values)
-can change list to set with set()
-set does not preserve order

LOOPS
-for loops
    -to run x times, for y in range(x - 1)
    -for x in y (y can be a list, set, etc, something with multiple values)
-while loops 
    -uses while keyword
-break: immediately exit loop (does not finish remaining iterations)
-continue: skip code below within loop, skip to the next iteration
-else: can use else to define code you would run after a loop is done UNLESS we break out of the function

