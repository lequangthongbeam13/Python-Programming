List = []
# MAIN FUNCTION
def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    namecount()
    shortest()
    longest()
    average()
#    #print(List)
    print("#### REPORT END ####")
    print("Program ending.")
    return None
# COUNT NAME IN TXT
def namecount():
    global a
    a = 0
    FileUser = input("Insert filename to read: ")
    with open(FileUser, "r") as file:
        for line in file:
            if line == "\n":
                continue
            else:
                a += 1
                List.append(line)
    print(f'Reading names from "{FileUser}".')
    print("Analysing names...")
    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print(f"Name count - {a}")
    return a
# FIND SHORTEST NAME
def shortest():
    ShortName = min(List, key = len)
    print(f"Shortest name - {len(ShortName) - 1} chars")
    return ShortName
# FIND LONGEST NAME
def longest():
    MaxName = max(List, key = len)
    print(f"Longest name - {len(MaxName) - 1} chars")
    return MaxName
# AVERAGE NAME
def average():
    global a
    LengthName = 0
    # print(f"Average name - {a}")
    for name in List:
        if name == "\n":
            continue
        else:
            LengthName += len(name)
            Average = ((LengthName - a) / a)
            format_length = "{:.2f}".format(Average)
    print(f"Average name - {format_length} chars")
    return None
main()