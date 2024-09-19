import random
List = ['r','p','s']
CChoice = random.choice(List)

#print(random.choice(List))


UserIn =str(input("Choose rock(r) , paper(p), or sissors(s): "))
print(CChoice)
if UserIn == CChoice:
    print ("Even")
elif UserIn == "r" and CChoice  == 'p':
    print ("You're lost") 
elif UserIn == "r" and CChoice == 's':
    print ("You're win")



elif UserIn == "p" and CChoice == 's':
    print ("You're lost")
elif UserIn == "p" and CChoice == 'r':
    print ("You win")



elif UserIn == "s" and CChoice == 'p':
    print ("You're win")
elif UserIn == "s" and CChoice == 'r':
    print ("You lost")
else:
    print("Type 'r','p' or 's'")





 