print("Program starting.")
Width = float(input("Insert width: "))
Height = float(input("Insert height: "))
def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    Area = Width * Height
    print(f"Area is {Area}²")
    return None
print("")
calcRectangleArea(Width, Height)
print("Program ending.")