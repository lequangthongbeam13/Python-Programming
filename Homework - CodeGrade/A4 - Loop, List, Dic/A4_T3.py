list =[]
print("Program starting.")
Snumber = int(input("\nInsert starting value: "))
Enumber = int(input("Insert stopping value: "))
print("\nStarting while-loop:")
while Snumber <= Enumber:
    list.append(Snumber)
    Snumber += 1
print (*list, sep = " ")
print("\nProgram ending.")