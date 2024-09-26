print("Program starting.")
list =[]
Snumber = int(input("\nInsert starting value: "))
Enumber = int(input("Insert stopping value: "))
print("\nStarting for-loop:")
for i in range(Snumber,Enumber+1):
    list.append(i)
print(*list,sep =" ")
print("\nProgram ending.")