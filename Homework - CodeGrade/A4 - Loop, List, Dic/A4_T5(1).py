print('Program starting.\n')
Nu1=int(input('Insert starting point: '))
Nu2=int(input('Insert stopping point: '))
Nu3=int(input('Insert inspection point: '))
print()
i=Nu1
if Nu1 >= Nu2:
    print('Starting point value must be less than the stopping point value.')
if Nu1 > Nu3 or Nu3 > Nu2:
    print('Inspection value must be within the range of start and stop.')
else:
    print(f'First loop - inspection with break:')
    if Nu1 == Nu3:
        print()
    for i in range(Nu1,Nu2):
        if i == Nu3:
            break
        elif i == Nu3-1:
            print(i)
        else:
            print(i,end=' ')
    print(f'Second loop - inspection with continue:')
    for i in range(Nu1,Nu2):
        if i == Nu3:
            continue
        elif i == Nu2-1:
            print(i)
        else:
            print(i,end=' ')
print('\nProgram ending.')