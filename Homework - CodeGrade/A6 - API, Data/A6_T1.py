def main():
    print("Program starting.")
    print("This program can read a file.")
    FileUser = input("Insert filename: ")
    with open(FileUser, "r") as file:
        content = file.read()
    print(f'#### START "{FileUser}" ####')
    print(content)
    print(f'#### END "{FileUser}" ####')
    print("Program ending.")
    return None
main()