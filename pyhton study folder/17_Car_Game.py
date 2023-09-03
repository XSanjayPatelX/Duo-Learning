answer = input("> ")

while True:
    if answer.lower() == "help":
        print("Start - start the car")
        print("Stop - stop the car") 
        print("Quit - exit game")
        answer = input.lower(("> "))

    elif answer.lower() == "start":
        print("Car started... Ready to go!")
        answer = input.lower(("> "))

    elif answer.lower() == "stop":
        print("Car stopped.")
        answer = input.lower(("> "))

    elif answer.lower() == "quit":
        print("Car stopped.")
        break
    else:
        print("Please try again")
        answer = input.lower(("> "))