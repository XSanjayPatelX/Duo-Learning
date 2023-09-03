# calculate number of characters within a string
course = "Python for Beginners"
print(len(course))

# .upper ext is called methods. A term used in Object-Orientated-Programming
# when a function belongs to something else or specific to some type of object. we refter to that object as a method
# len and print dont belong to strings because they are general purpose functions
# .upper is specific to a string, it is refered to a method
course = "Pyhton for Beginners"
print(course.upper()) # all characters are upper case
print(course.lower()) # all characters are lower case
print(course) # all characters keep the same format as written in the varaible

# find a character or sequence of characters within a string
course = "Python for Beginners"
print(course.find("P")) # this will return the first index of the character
print(course.find("o")) # the index of the "o" is 4
print(course.find("O")) # get -1 because there is no uppercase O in the string
print(course.find("Beginners")) # can pass a sequence of characters
print(course.replace("Beginners", "Absolute Beginners")) # will replace the world Beginners with Absolute Beginners
print(course.replace("P", "J")) # Can replace characters as well
print("Python" in course) # check to see if word is in the course variable. A boolean expression, true or false
# Find method returns the index of character or sequence
# In operator produces a boolean value, do we have this or not

len() # Count number of characters in a string
course.upper() # Convert to uppercase 
course.lower() # Convert to lowercase
course.title() # First character in every word is uppercase
course.find() # return index of character or sequence
course.replace() # replace character and words in a string
"...." in course # characters in a string true or not. Boolean