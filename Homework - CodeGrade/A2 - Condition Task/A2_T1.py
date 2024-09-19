print ("Program starting.")
Name = input(("What is your name: "))
Num1 = float(input(("Enter a floating point number: ")))
Num2 = float(input(("Enter second floating point number: ")))
Mul = round(Num1 * Num2,2)
FormattedString = "{0} you gave numbers {1} and {2}\n"\
    "Multiplying first and second number will result in product {3:.2f}".format(Name,Num1,Num2,Mul)
print (FormattedString)
print ("Program ending.")