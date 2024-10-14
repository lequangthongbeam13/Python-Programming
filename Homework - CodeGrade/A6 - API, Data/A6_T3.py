def main():
    print("Program starting.")
    print("This program can copy a file.")
    SourceFile = input("Insert source filename: ")
    Destination = input("Insert destination filename: ")
    with open(SourceFile, "r") as firstfile, open(Destination, "w") as secondfile:
        for line in firstfile:
            secondfile.write(line)
    print(f"Reading file '{SourceFile}' content.")
    print("File content ready in memory.")
    print(f"Writing content into file '{Destination}'.")
    print("Copying operation complete.")
    print("Program ending.")
    return None
main()