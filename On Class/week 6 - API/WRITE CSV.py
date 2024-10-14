import csv
# Data to be written to the CSV file
data = [
["Name", "Age", "Town"],
["Mari", 40, "Tampere"],
["Johanna", 49, "Espoo"],
["Katja", 47, "Turenki"]
]
# Writing to the CSV file
with open("data.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print("Data written to data.csv")