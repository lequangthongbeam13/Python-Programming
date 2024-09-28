fruits = ['pi','apple','pear', 'banana', 'kiwi', 'apple', 'ba']
# n = len(fruits[0]) + len(fruits[1]) + len(fruits[2]) + len(fruits[3]) + len(fruits[4]) + len(fruits[5]) + len(fruits[6])
# print (n)
list = []
m = 0
while m < len(fruits):
    list.append(len(fruits[m]))
    m += 1
Sum = sum(list)    
print (Sum)





    

    

