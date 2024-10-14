import json
# New user data to be added
new_user ={"login": "user3", "password": "pass3"}
# Reading the existing data from the JSON file
with open("data.json", "r") as file:
    data= json.load(file)
# Adding the new user to the list of users
    data["users"].append(new_user)
# Writing the updated data back to the JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
print("Updated data written to data.json")