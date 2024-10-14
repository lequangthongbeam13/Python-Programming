Word = ""
def main():
    print("Program starting.")
    WordInput = input("Insert word: ")
    print("") 
    Word = WordInput
    frameWord(Word)
    print("\nProgram ending.")
def frameWord(Pword):
        numofCharsB = "**" + "*" * len(Pword) + "**"
        print(numofCharsB)
        print("*", Pword, "*")
        print(numofCharsB)
        return None
main()
