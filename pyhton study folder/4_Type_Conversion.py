# ask year we was born, then calculate our age and print it in the terminal
birth_year = int(input("What year was you born? "))
age = 2023 - birth_year
print(age)

# functions
int() # Convert string into integer
float() # Convert string into a float or a number with a decimal point
bool() # Convert string into a boolean value

# useful function to get type of variable
# whenever you use the input function, you always get a string. if you are
# inputting a numerical value, always convert sting into an integer or float
birth_year = int(input("What year was you born? "))
print(type(birth_year))
age = 2023 - birth_year
print(type(age))
print(age)

# Exercise
# Ask the user their weight(in pounds), convert it to kilograms and print to terminal
user_weight_lbs = float(input("What is your weight? "))
user_weight_kg = user_weight_lbs * 0.45
print("Your weight is " + str(user_weight_kg))