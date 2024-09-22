print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
Name = input("Before the menu, please insert your name: ")
print("\nOptions:")
print("1 - Print welcome message")
print("0 - Exit")
Choice = input("Your choice: ")
if int(Choice) == 1:
    print(f"Welcome {Name}!")
elif int(Choice) == 0:
    print("Exiting...")
else:   
    print("Unknown option.")
    
print("\nProgram ending.")