# Positional arguments, there posission or order matters
def greet_userr(first_name, last_name): 
    print(f'Hi there {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_userr("Smith", "John")
print("Finish")

# Keyword arguments
def greet_userrr(first_name, last_name): 
    print(f'Hi there {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_userrr(last_name="Smith", first_name="John")
print("Finish")

# passing numerical values
def greet_use(first_name, last_name): 
    print(f'Hi there {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_use(last_name="Smith", first_name="John")
calc_cost(total=50, shipping=5, discount=0.1) # keyword arguments, name of parameters
print("Finish")