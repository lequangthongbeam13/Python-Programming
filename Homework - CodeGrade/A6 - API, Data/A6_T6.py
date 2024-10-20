import codecs
SEPARATOR = ";"
CollectWord = ""
CipherWord = ""
def AskInput(PPrompt: str):
    Feed = input(f"{PPrompt}")
    return Feed
def CollectWords():
    global CollectWord
    while True:
        InputWord = AskInput("Insert row(empty stops): ")
        if InputWord == "":
            break
        else:
            CollectWord += InputWord + "\n"
    return CollectWord
def ROT13Conversion():
    global CipherWord
    CipherWord = codecs.encode(CollectWord, 'rot13')
    print(CipherWord)
    return CipherWord
def Writetext():
    dataName = input("Insert filename to save: ")
    if dataName == "":
        print("File name not defined.")
        print("Aborting save operation.")
    else:
        with open(dataName, "w") as file:
            file.write(CipherWord)
        print("Ciphered text saved!")
    return None
def main():
    print("Program starting.")
    print("\nCollecting plain text rows for ciphering.")
    CollectWords()
    print("\n#### Ciphered text ####")
    ROT13Conversion()
    print("#### Ciphered text ####")
    Writetext()
    print("Program ending.")
    return None
main()