import requests
base_url = "https://rata.digitraffic.fi/api/v1/live-trains/station"
departure_station = input("Departure City: ")
arrival_station = input("Arrival City: ")

url = f"{base_url}/{departure_station}/{arrival_station}"
response = requests.get(url)
print(response)
# Check if the request was successful
if response.status_code == 200:
# Parse the JSON response
    trains = response.json()
    for train in trains:
        train_number = train["trainNumber"]
        # Initialize variables to store departure and arrival times
        scheduled_departure = None
        actual_departure = None
        scheduled_arrival = None
        actual_arrival = None
        # Find the departure and arrival times from the timetable rows
        for row in train["timeTableRows"]:
            if row["stationShortCode"] == departure_station and row["type"] == "DEPARTURE":
                scheduled_departure = row["scheduledTime"]
            if row["stationShortCode"] == arrival_station and row["type"] == "ARRIVAL":
                scheduled_arrival = row["scheduledTime"]
        print(f"\nTrain Number: {train_number} "
            f"\nDeparture Date: {scheduled_departure[0:10]} - Time: {scheduled_departure[11:16]} "
            f"\nArrival: {scheduled_arrival[0:10]} - Time: {scheduled_arrival[11:16]}")
else:
    print(f"Failed to retrieve train data. Status code: {response.status_code}")