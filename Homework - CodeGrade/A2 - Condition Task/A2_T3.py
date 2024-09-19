print ("Program starting.")
Len1 = input("Insert first word: ")
Len2 = input("Insert second word: ")
Sen = "1st word is {0} characters long.\n"\
    "2nd word is {1} characters long.\n"\
    "Words together makes one closed compound '{2}'.".format(len(Len1),len(Len2),Len1+Len2)
print (Sen)
print("Program ending.")