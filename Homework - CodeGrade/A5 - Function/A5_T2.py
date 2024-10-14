def frameWord(PWord):
    print("*" * len(PWord) + "****")
    print(f"* {PWord} *")
    print("*" * len(PWord) + "****")
def main():
    print("Program starting.")
    Text = str(input("Insert word: "))
    print("")
    frameWord(Text)
    print("")
    print("Program ending.")
    return None

main()