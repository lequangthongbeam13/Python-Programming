print("Program starting.")
ListWords = []
# 1. InsertWord
def InsertWords(Word = ""):
    Word = input("Insert word: ")
    ListWords.append(Word)
# 2. ShowWord
def ShowWords():
    if len(ListWords) == 0:
        print("Current word - \"\"")
    else:
        Cur = ListWords[0]
        print(f'Current word - "{Cur}"')
# 3. Reverse
def Reverse():
    if len(ListWords) == 0:
        print("Word reversed - \"\"")
    else:
        Rev = str([i[::-1] for i in ListWords])[2:-2]
        print(f'Word reversed - "{Rev}"')
# Menu
def main():
    print("Options:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")
    return None


while True:
    main()
    Choice = int(input("Your choice: "))
    if Choice == 1:
        InsertWords()
        print("")
    elif Choice == 2:
        ShowWords()
        print("")
    elif Choice == 3:
        Reverse()
        print("")
    elif Choice == 0:
        print("Exiting program.")
        break
    else:
        print("Unknown option! try again.")
        print("")
print("\nProgram ending.")