print("Program starting.")
print("\nCheck multiplicative persistence.")
number = int(input("Insert an integer: "))
product = 1
persistence = 0
list = []

while number > 9:
    for digit in range(0, len(str(number))):
        list.append(int(str(number)[digit]))
        product *= int(str(number)[digit])
        
    
    print(*list,sep= " * ", end=" = ")
    print(product)
    persistence += 1
    number = product
    product = 1
    del list[0:len(str(number))+4]
print("No more steps.")
print(f"\nThis program took {persistence} step(s)")
print("\nProgram ending.")
