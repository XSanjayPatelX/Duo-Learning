# Add to list
numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

# Insert let you choose position of value in the list
numbers = [5, 2, 1, 7, 4]
numbers.insert(0, 10)
print(numbers)

# Remove items in list
numbers = [5, 2, 1, 7, 4]
numbers.remove(5)
print(numbers)

# Remove all items from list
numbers = [5, 2, 1, 7, 4]
numbers.clear()
print(numbers)

# Pop method, remove last item in a lost
numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)

# Check for existance of an item in a list
numbers = [5, 2, 1, 7, 4]
print(numbers.index(5))
print(numbers)

# Another way to check existance of an item in a list
# This does not generate an error message
numbers = [5, 2, 1, 7, 4]
print(50 in numbers)

# Count number in a list
numbers = [5, 2, 1, 5, 7, 4]
print(numbers.count(5))

# Sort your list in order
numbers = [5, 2, 1, 5, 7, 4]
numbers.sort()
print(numbers)

# Sort your list discending order
numbers = [5, 2, 1, 5, 7, 4]
numbers.sort()
numbers.reverse()
print(numbers)

# copy method
numbers = [5, 2, 1, 5, 7, 4]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)
print(numbers)

# Exercise
# Write a program to remove the duplicates in a list
# correct, long method
numbers1 = [2, 2, 4, 6, 3, 4, 6, 1]
numbers2 = numbers1.copy()
numbers2.remove(2)
numbers2.remove(4)
numbers2.remove(6)
print(numbers2)

# Correct, short method
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)