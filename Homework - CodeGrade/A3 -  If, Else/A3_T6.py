print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")
print("\nOptions:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
Choice = input("Your choice: ")
if int(Choice) == 1:
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    Choice = input("Your choice: ")
    if int(Choice) == 1:
        Value1 = float(input("Insert meters: "))
        print(f"{Value1:.1f} m is {(Value1/1000):.1f} km")
    elif int(Choice) == 2:
        Value1 = float(input("Insert kilometers: "))
        print(f"{Value1:.1f} km is {(Value1*1000):.1f} m")
    elif int(Choice) == 0:
         print("Exiting...")
    else:
         print("Unknown option.")
         
         
elif int(Choice) == 2:
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    Choice = input("Your choice: ")
    if int(Choice) == 1:
        Value1 = float(input("Insert grams: "))
        print(f"{Value1:.1f} g is {(Value1*0.002205):.4f} lb")
    elif int(Choice) == 2:
        Value1 = float(input("Insert pounds: "))
        print(f"{Value1:.1f} lb is {round(Value1*453.6,1)} g")
    elif int(Choice) == 0:
         print("Exiting...")
    else:
         print("Unknown option.")
elif int(Choice) == 0:
        print("\nExiting...")
else: 
    print("Unknown option.")
print("\nProgram ending.")