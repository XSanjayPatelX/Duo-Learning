# Solution to exercise

weight = int(input("Enter your weight either in pounds or kilograms: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} killos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")