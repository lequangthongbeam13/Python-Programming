print("Simple menu")
print ("Select from the list:")
L1 = "1. Login"
L2 = "2. Go to settings"
L3 = "3. Logout"
print(f"{L1}\n{L2}\n{L3}\n")
UserInput = int(input("Choose your options: "))

if UserInput == 1:
    print("Program started")
elif UserInput == 2:
    print ("Settings")
elif UserInput == 3:
    print ("Logged out")
else:
    print("User input not recognized")
