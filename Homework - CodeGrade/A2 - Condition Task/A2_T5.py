print("Program starting.\n")
UserI = input("Insert a closed compound word: ")
print(f"The word you inserted is '{UserI}' and in reverse it is '{UserI[::-1]}'.")
print(f"The inserted word length is {len(UserI)}")
print(f"Last character is '{UserI[-1]}'\n")
print("Take substring from the inserted word by inserting...")
Point = UserI[int(input("1) Starting point: ")):int(input("2) Ending point: ")):int(input("3) Step size: "))]
print(f"\nThe word '{UserI}' sliced to the defined substring is '{Point}'.")
print("Program ending.")

