print("Program starting.")
list = []
Num = int(input("Insert a positive integer: ")) 
# while True:
#     if Num % 2 == 0:
#         print (Num / 2)
#     elif Num % 2 != 0:
#         print(Num * 3 +1)

while True:
    list.append(Num)
    if Num == 1:
        break
    elif Num % 2 == 0:
        Num = Num // 2       
    else:
        Num = ((Num * 3 +1))
        
print (*list, sep=" -> ")
print ("Sequence had", len(list)-1, "total steps.")






print("\nProgram ending.")