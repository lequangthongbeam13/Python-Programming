DELIMITER = ""
List = []
Characters = []

def collectWords():
    while True:
        UserWord = input("Insert word(empty stops): ")
        if UserWord == "":
            # print(f"- {len(List)} Words")
            # print(f"- {sum(Characters)} Characters")
            # Avg = sum(Characters)/len(List)
            # print(f"{0:.2f} Average word length".format(Avg))
            break
        else:
            analyseWords(UserWord)
    return UserWord
def analyseWords(Word):
    List.append(Word + DELIMITER)
    Characters.append(len(Word))
    return Word
def main():
    print("Program starting.")
    collectWords()
    print(f"- {len(List)} Words")
    print(f"- {sum(Characters)} Characters")
    SumWord = sum(Characters) / len(List)
    print("-", format(SumWord, '.2f'), "Average word length")
    print("Program ending.")
    return None
main()