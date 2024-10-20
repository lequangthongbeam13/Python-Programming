FileNumber = 0
SFile = 0
FileUser = ""
ContentList = []
SEPARATOR = ";"
def Readfile(Name):
    global FileNumber
    with open(Name, "r") as file:
        for line in file:
            if line == "\n":
                continue
            else:
                FileNumber += 1
                ContentList.append(line)
    return file

def CountFile():
    FileNumber = len(ContentList)
    return FileNumber

def SumFile():
    global SFile
    SFile = sum(map(int, ContentList))
    return SFile


def GreatestFile():
    ContentList.sort()
    Greatest = ContentList[-1].strip()
    return Greatest

def AvgFile():
    Avg = SumFile() / CountFile()
    AvgFormat = "{:.2f}".format(Avg)
    return AvgFormat

def ReadValue() -> str:
    global SFile
    Values: str = ""
    Values += str(FileNumber) + SEPARATOR
    Values += str(SumFile()) + SEPARATOR
    Values += str(GreatestFile()) + SEPARATOR
    Values += str(AvgFile())
    print(Values)
    return Values
def main():
    print("Program starting.")
    FileUser = input("Insert filename: ")
    Readfile(FileUser)
    print("#### Number analysis - START ####")
    print(f'File "{FileUser}" results:')
    print("Count;Sum;Greatest;Average")
    ReadValue()
    print("\n#### Number analysis - END ####")
    print("Program ending.")
    return None
main()