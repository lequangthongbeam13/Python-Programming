Pname =""
def main():
    global Pname
    print("Program starting.")
    def askName():
        PName = input("Insert name: ")
        def greetUser(PName):
            print(f"Hello {PName}!")
            return PName
        greetUser(PName)
    askName()
    print("Program ending.")
    return Pname
main()