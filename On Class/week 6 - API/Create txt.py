# Data to be written to the text file
data = """ HELLO """
# Writing to the text file
with open("data.txt", "w") as file:
    file.write(data)
    print("Data written to data.txt")