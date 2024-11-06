Number = []
NumberUser = ""
def seperatenumber():   
    global NumberUser
    global Number
    Invalid =""
    NumberUser = (input("Insert comma separated integers: "))
    if NumberUser == "b":
            print (f"Invalid value '{NumberUser}' detected.")
            print("No values to analyse.")
    else:
        sep = NumberUser.split(",")
        for i in range(len(sep)):
            if sep[i].isnumeric():
                Number.append(sep[i])
            else:
                Invalid = sep[i]
                print (f"Invalid value '{Invalid}' detected.")
        for i in range(len(Number)):
            Number[i] = int(Number[i])
        print(f"There are {len(Number)} integers in the list.")
        SumNumber = sum(Number)
        if SumNumber %2 == 0:
            print(f"Sum of the integers is {SumNumber} and it's even")
        else:
            print(f"Sum of the integers is {SumNumber} and it's odd")
    return None
def main():
    print("Program starting.")
    seperatenumber()
    print("Program ending.")
    return None
main()