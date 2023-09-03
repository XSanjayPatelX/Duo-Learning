# Adding one loop inside another
# (x, y)
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)

# X is 0
# Y is an iner-loop, the first iteration
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

# Exercise
# Draw F in the command using x and for loops
# one solution
numbers = [5, 2, 5, 2, 2]

for f in numbers:
    print("x" * f)

# second solution
numbers = [5, 2, 5, 2, 2]

for f in numbers: 
    output = "" # reset output variable to empty string
    for count in range(f): 
        output += "x"
    print(output)

print("\n")
# Exercise 2, print L
number = [1, 1, 1, 1, 1, 1, 9]

for l in number:
    output = ""
    for count in range(l):
        output += "x"
        print(output)