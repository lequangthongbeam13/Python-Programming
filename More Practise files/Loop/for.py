SNumber = int(input("Starting number: "))
ENumber = int(input("Ending number: "))
n = (ENumber - SNumber) +1

for i in range(n):
    SNumber += 1
    print(SNumber - 1)