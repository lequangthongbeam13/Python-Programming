def greeting_airport(person, age):
    print(f"How do you do{person}")
    if age >=18:
        print("Welcome on you flight.")
    else:
        print("I'm sorry, you are nor allowed to fly on your own.")
        print(f"You need tp wait for {18-age} years.")
greeting_airport(" Mira",47)
greeting_airport(age = 7, person=" Maija")

# print (person)
# print(Number1)