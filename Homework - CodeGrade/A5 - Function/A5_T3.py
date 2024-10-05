def main():
    print("Program starting.")
    def askName():
        PName = input("Insert name: ")
        def greetUser(PName):
            print(f"Hello {PName}!")
            return None
        greetUser(PName)
    askName()
    print("Program ending.")
    return None
main()