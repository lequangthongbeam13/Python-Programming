print("Program starting.")
list =[]
characters =[]
i = 0
Word = input("\nInsert word (empty stops): ")
list.append(Word)
while len(Word) != 0 or i < len(characters):
    Word = input("Insert word (empty stops): ")
    list.append(Word)
    characters.append(len(list[i]))
    i += 1
SumChars = sum(characters)
print("\nYou inserted:")
print("-",(len(list)-1),"words")
print("-",SumChars,"characters")
print("\nProgram ending.")