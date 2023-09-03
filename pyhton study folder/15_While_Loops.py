# While loops are used to execute a block of code multiple times
# Useful in building interactive programs and games


i = 1 
while i <= 5: # condition is true because i is less than 5
    print(i) # print i
    i = i + 1 # i is incremented by 1 until the value equals 5. loop will be terminated when i gets higher than 5  
print("Done") # This will be printed into the console when the while loop is false


i = 1
while i <= 5:
    print('*' * i) # prints out astrid/star instead of the number but the condition is still the same
    i = i + 1
print("Done")