list=[]
i = 1
def prime_Num (value):
    is_prime = True
    for i in range(value):
        i += 1
        if value % i == 0:
            is_prime = False
            # print(i)
    if(len(list)) == 2:
        print("This is a prime number")
    else:
        print("This is NOT a prime number")

TestNum = int(input("Enter Number: "))
prime_Num(TestNum)
while True:
    # prime_Num(value)
    
    if input(("Do you want to test another number?(y/n): ")) != "y":
        break
    else:
        list = []
        TestNum = int(input("Enter Number: "))
        prime_Num(TestNum)
        
