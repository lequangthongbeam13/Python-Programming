import re
print("Program starting.")
print("\nOptions:")
print("1 - Celcius to Fahrenheit")
print("2 - Fahrenheit to Celcius")
print("0 - Exit")
Choice = input("Your choice: ")
if int(Choice) == 1:
    Temp = float(input("Insert the amount of Celcius: "))
    print(f"{Temp:.1f} °C equals to {Temp*1.8+32} °F")
elif int(Choice) == 2:
    Temp = float(input("Insert the amount of Fahrenheit: "))
    print(f"{Temp:.1f} °F equals to {round((Temp-32)*5/9,1)} °C")
elif int(Choice) == 0:
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")