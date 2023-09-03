# how to handle errors in program
#age = int(input('Age: '))
#print(age)
# try, except, used to handle erros and not crash program

# exception is a kind of error that crashes a program
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('age cannot be zero')
except ValueError:
    print('Invalid value')

