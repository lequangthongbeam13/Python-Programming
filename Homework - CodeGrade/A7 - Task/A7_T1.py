Number = []
def main() -> None:
    print("Program starting.")
    Collectnumbers()
    DisplayNumbers() 
    print("Program ending.")
    return None
def Collectnumbers():
    print("Collect positive integers.")
    while True:
        UserNum = str(input("Insert positive integer(negative stops): "))
        if UserNum == "-1" and len(Number) == 0:
            print("Stopped collecting positive integers.")
            print("No integers to display.")
            break
        elif UserNum == "-1":
            print("Stopped collecting positive integers.")
            print (f"Displaying {len(Number)} integers:")
            break
        elif UserNum.isnumeric() == True:
            Number.append(UserNum)
    return UserNum
def DisplayNumbers():
    i = 0
    for i in range(len(Number)):
        print(f"- Index {i} => Ordinal {i+1} => Integer {(Number[i])}")
    return Number
main()