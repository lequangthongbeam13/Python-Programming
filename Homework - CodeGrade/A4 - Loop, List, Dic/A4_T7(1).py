print('Program starting.')

print('\nCheck multiplicative persistence.')

Num=input('Insert an integer: ')
Step=0
while len(Num) != 1:
    Step+=1
    Val1=1
    for i in range(len(Num)):
        if i == len(Num)-1:    
            print(Num[i],end=' = ')
        else:
            print(Num[i],end=' * ')
        Val1*=int(Num[i])
    print(Val1)
    
print('No more steps.\n')
print(f'This program took {Step} step(s)')
print('\nProgram ending.')