print("Program starting.")
print("String comparisons")
Word = str(input("Insert first word: "))
Char = str(input("Insert a character: "))
if Char in Word:
    print(f'Word "{Word}" contains character "{Char}"')
else:
    print(f"Word \"{Word}\" doesn't contain character \"{Char}\"")
Word2 = str(input("Insert second word: "))
if Word < Word2:
    print(f"The first word \"{Word}\" is before the second word \"{Word2}\" alphabetically.")
elif Word2 < Word:
    print(f"The second word \"{Word2}\" is before the first word \"{Word}\" alphabetically.")
else:
    print(f"Both inserted words are the same alphabetically, \"{Word}\"")
print("Program ending.")