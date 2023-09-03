# comparison operators are used when you want to compare a variable with a value

# If temperature is greater than 30, its a hot day
# Otherwise if its less than 10, its a cold day
# Otherwise its neither hot nor cold

# > greater than
# >= greater than or equal to
# < less than 
# <= less than or equal to
# == equality operator
# != not equal operator 

temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# Exercise
# If name is less than 3 characters long, name must be at least 3 characters 
# Otherwise if its more than 50 characters long, name can be a maximum of 50 characters
# Otherwise, name looks good

# Mine, wrong
name_characters = 32

if name_characters < 3:
    print("Name must be at least 3 characters long")
elif name_characters > 50:
    print("Name can be a maximum of 50 characters long")
else:
    print("Name looks good!")

# Correct way to do exercise
name = "Hamza Nawaz"
if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters long")
else:
    print("Name looks good!")