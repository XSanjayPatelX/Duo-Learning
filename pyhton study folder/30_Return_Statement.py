# function that return the result 

def square(number):
    return number * number


result = square(3)
print(result)

# call function directly inside a print function without define another variable

def squaree(number):
    return number * number


print(squaree(3))

# Dont use return statement
def squareee(number):
    print(number * number)


print(squareee(3))

# All function in python return none
# Return result using return statement