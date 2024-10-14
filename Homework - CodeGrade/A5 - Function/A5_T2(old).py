def main():
    print("Program starting.")
    Word = input("Insert word: ")
    print("")
    def frameWord(Pword):
        numofCharsB = "**" + "*" * len(Pword) + "**"
        print(numofCharsB)
        print("*", Pword, "*")
        print(numofCharsB)
        return None
    frameWord(Word)
    print("\nProgram ending.")
    return None
main()