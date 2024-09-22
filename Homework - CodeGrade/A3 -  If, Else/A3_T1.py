print("Program starting.")
print("Insert two integers.")
Num1 = int(input("Insert first integer: "))
Num2 = int(input("Insert second integer: "))
print("Comparing inserted integers.")
if Num1 > Num2: 
    print("First integer is greater.")
elif Num1 < Num2:
    print("Second integer is greater.")
else: 
    print("Integers are the same")
print("\nAdding integers together")
print(f"{Num1} + {Num2} = {Num1+Num2}")
print("\nChecking the parity of the sum...")
if (Num1+Num2) %2 == 0:
    print("Sum is even.")
else: 
    print("Sum is odd.")
print("Program ending.")