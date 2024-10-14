def main():
    print("Program starting.")
    FirstName = input("Insert first name: ")
    LastName = input("Insert last name: ")
    FileName = input("Insert filename: ")
    with open(FileName, "w") as file:
        file.write(FirstName + "\n" + LastName + "\n")
    print("Program ending.")
    return None
main()