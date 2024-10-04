def letter(Lastname, Firstname):
    print (Firstname.capitalize() + " " + Lastname.capitalize())
Lastname = input("Your First Name: ")
Firstname = input("Your Last Name: ")
if len(Firstname) ==0 and len(Lastname) == 0:
        print("You didn't provide valid inputs.")
else:
    letter(Firstname,Lastname)

