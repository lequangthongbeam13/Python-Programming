Number = []
k_number = 1
while True:
    if k_number % 2 == 0:
        Number.append(k_number)
        if len(Number) <5:
            break
    k_number += 1
print (Number)
print(k_number)
