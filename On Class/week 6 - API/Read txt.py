# Reading from the text file
with open("data.txt", "r") as file:
    content = file.read()
print("Content of data.txt:")
print(content)