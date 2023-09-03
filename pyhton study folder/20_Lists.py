names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
print(names)

names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
print(names[1])

names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
print(names[2:4])

names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
names[0] = "Jon" # replace word
print(names)

#Exercise
# Write a program to find the largest number in a list

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)