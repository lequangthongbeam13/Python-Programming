import json
# Initial data to be written to the JSON file
data = {
"users": [
{"login": "user1", "password": "pass1"},
{"login": "user2", "password": "pass2"}
]
}
# Writing to the JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
print("Initial data written to data.json")