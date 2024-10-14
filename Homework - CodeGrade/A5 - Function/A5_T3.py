Name = ""
def main():
    global Name
    print("Program starting.")
    askName()
    greetUser(Name)
    print("Program ending.")
    return None
def askName():
    global Name
    Name = input("Insert name: ")
    return Name
def greetUser(PName):
    global Name
    print(f"Hello {PName}!")
    return None
main()
