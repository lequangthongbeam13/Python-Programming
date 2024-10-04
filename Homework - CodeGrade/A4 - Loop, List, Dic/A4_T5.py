print("Program starting.")
Firstloop =[]
Secondloop =[]
Str = int(input("\nInsert starting point: "))
End = int(input("Insert stopping point: "))
Ins = int(input("Insert inspection point: "))


if Str >= End:
     print("\nStarting point value must be less than the stopping point value.")
elif Ins < Str or Ins > End:
        print("Inspection value must be within the range of start and stop.")
else:
    for i in range(Str, Ins):
        Firstloop.append(i)
    print("\nFirst loop - inspection with break:")
    print(*Firstloop)
    
    for k in range(Str, End):
        if k == Ins:
            continue
        Secondloop.append(k)
    print("Second loop - inspection with continue:")
    print(*Secondloop)


print("\nProgram ending.")