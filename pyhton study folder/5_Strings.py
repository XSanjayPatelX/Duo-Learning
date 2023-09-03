# Use double quotes when adding single quotes to string
# Use single quotes when adding double quotes to string
#course = "Python's Course for Beginners"
#course_double = 'Pyhton Course for "Beginners"'
#print(course)
#print(course_double)

# define string with multiple lines
# this is a multiline string
#course = ''' 
#Hi John, 

#Here is our first email to you.

#Thank you,
#The support team

#'''
#print(course)

# other characteristics of strings within python
course = 'Pyhton for beginners'
print(course[0]) # Python starts from 0 so P is the letter it will print out
print(course[-1]) # "s" will be the character at the end. This is the index of the last character
print(course[-2]) # "r" will be the second last character at the end
print(course[0:3]) # Python will print out the characters starting from 0-2
print(course[0:]) # If you dont put anything for the end index, python will return all the characters
print(course[1:]) # it will exclude the first character and start from "y"
print(course[:5]) # python interperator will assume 0 is the starting index
print(course[:]) # 0 will be the start index and the length of the string will be the end index

# copy or cloan your string
course = 'Pyhton for beginners'
another = course[:] # This variable will copy our first variable and return all of the characters
print(another)

# Exercise
name = 'Jennifer'
print(name[1:-1]) # "r" will be excluded and "J" will be excluded
# answer on terminal
print("ennife") 