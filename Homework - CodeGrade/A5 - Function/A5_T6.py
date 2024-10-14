print("Program starting.")
n = 0
Choice = ""
def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None
def askChoice():
    global Choice
    Choice = (input("Your choice: "))
    return (Choice)
def main():
    while True:
        global Choice
        global n
        showOptions()
        askChoice()
        if (Choice) == "2":
            n += 1
            print("Count increased!")
            print("")
        elif (Choice) == "3":
            n = 0
            print("Cleared count!")
            print("")
        elif (Choice) == "1":
            print(f"Current count - {n}")
            print("")
        elif (Choice) == "0":
            print("Exiting program.")
            break
        elif (Choice) == (Choice.isnumeric()) == False:
            print("Unknown option!")
            print("")
        else:
            print("Unknown option!")
            print("")
    return None
main()
print("\nProgram ending.")