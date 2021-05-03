# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive.
# The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(string):
    x_arr = []
    o_arr = []
    match = False

    for char in string:
        if (char == "x" or char == "X"):
            x_arr.append(char)
        elif (char == "o" or char == "O"):
            o_arr.append(char)
        elif(char == "0"):
            match = True

    if (len(x_arr) == len(o_arr)):
        match = True

    if (match):
        return match
    else:
        return match
    
print(xo("xoxo"))
print(xo("xo0"))
print(xo("xxxoo"))
