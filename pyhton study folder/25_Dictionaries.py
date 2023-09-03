# store information
# customer
# name
# email
# phone number
# key values pair
# dictionaries store key values pair
# Each key should be unique
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
} # define a dictionary with {}
print(customer["name"])
print(customer.get("name")) # does not give error
print(customer.get("birthdate", "Jan 1 1980")) # Get defult value

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
} # define a dictionary with {}
customer ["name"] = "Jack Smith" # can update values of key word name
print(customer["name"])

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
} # define a dictionary with {}
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])

# Exercise
# Program thats asks for our phone number. Type it into digits and converts it into words

phone_number = input("Phone: ") # Take input from user
numbers = {  # Dictionary holding key values
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Sevem",
    "8": "Eight",
    "9": "Nine"
}
output = "" # Empty string/ output string
for digit in phone_number: # look for characters in phone_number variable
    output += numbers.get(digit, "!") + " " # get method used so program does not yell at them. pass digit as key and
# supply defult value, "!", if dictionary does not have value. space at end so words are not close together, " ". 
print(output) # Print number out in words