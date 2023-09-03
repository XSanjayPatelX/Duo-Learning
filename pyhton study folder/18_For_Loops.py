# iterate over each character in a string and do something with it
for item in "Python":
    print(item)

# Define list using square brackets []
for item in ["Mosh", "John", "Sarah"]:
    print(item)

for item in [1, 2, 3, 4]:
    print(item)

# Creates a range of numbers
# Create an object that will spit out a new number
for item in range(10):
    print(item)

# Range of numbers
for item in range(5, 10):
    print(item)

# Take 2 steps forward
for item in range(5, 10, 2):
    print(item)

# Exercise
# Write a program to calculate the total cost in a shopping cart

prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(total)
print(f"Total: {total}")