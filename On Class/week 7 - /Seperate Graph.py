import pandas as pd
import matplotlib.pyplot as plt
import requests
UTemperatue = []
UMovement=[]
UTime = []
url ="https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=20"
response = requests.get(url)
print(f"Status code: {response.status_code}")
data = response.json()

for entry in data["feeds"]:
    movement_value = entry ["field1"]
    temp_value = entry["field2"]
    time_value = entry["created_at"]

    # time_value = entry["created_at"]
    UTemperatue.append(temp_value)
    UMovement.append(movement_value)
    UTime.append(time_value)

    # print(f"Movement value: {movement_value}")
    # print(f"Temperature value: {temp_value}")
    # print(f"At: {time_value}")
data = {
    'Temperature': UTemperatue,
    'Movement': UMovement,
    "Time": UTime
    }

df = pd.DataFrame(data)
print (df.to_string(index =False))

# df.set_index('Temperature', inplace=True)
# print (df)
# Plotting
plt.figure(figsize=(10, 5))
plt.plot(df['Temperature'], label='Temperature')
# plt.plot(df['Movement'], label='Movement')
# plt.xlabel(UTime, label = 'Time')
plt.ylabel('Values')
plt.title('Temperature Over Time')
plt.legend()
plt.show()



f1 = plt.figure()
f2 = plt.figure()
ax1 = f1.add_subplot(111)
ax1.plot(range(0,10))
ax2 = f2.add_subplot(111)
ax2.plot(range(10,20))
plt.show()