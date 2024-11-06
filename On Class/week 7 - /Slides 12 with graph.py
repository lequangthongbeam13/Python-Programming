import pandas as pd
import matplotlib.pyplot as plt
import requests
UTemperatue = []
UMovement=[]
url ="https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=20"
response = requests.get(url)
print(f"Status code: {response.status_code}")
data = response.json()

for entry in data["feeds"]:
    movement_value = entry ["field1"]
    temp_value = entry["field2"]
    # time_value = entry["created_at"]
    UTemperatue.append(temp_value)
    UMovement.append(movement_value)

    # print(f"Movement value: {movement_value}")
    # print(f"Temperature value: {temp_value}")
    # print(f"At: {time_value}")
data = {
    'Temperature': UTemperatue,
    'Movement': UMovement
    }

df = pd.DataFrame(data)
print (df.to_string(index =False))

# df.set_index('Temperature', inplace=True)
# print (df)




# Example data
data = {
'Temperature': UTemperatue,
'Movement': UMovement
}
# Create DataFrame
df = pd.DataFrame(data)
# Plotting
plt.figure(figsize=(10, 5))
plt.plot(df['Temperature'], label='Temperature')
plt.plot(df['Movement'], label='Movement')
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Temperature and Movement Over Time')
plt.legend()
plt.show()

