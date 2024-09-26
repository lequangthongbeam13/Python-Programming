# for i in range (1,10):
#     print (i)

# for i in range (1,10):
#     print(i,end =' ') 

EnNum = int(input("Enter ending number:"))
i= 0
for i in range (EnNum):
    if i %2 == 0:
        print (i+2)
        i += 1