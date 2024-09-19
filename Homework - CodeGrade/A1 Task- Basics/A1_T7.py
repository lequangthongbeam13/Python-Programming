print("Calculate fuel consumption.")
Feed = int(input("Enter travel distance(kilometers): "))
Distance = Feed
Feed = int(input("Enter fuel usage(liters): "))
FuelUsage = Feed
Comsumption = int(100 * FuelUsage / Distance)
print ("Fuel consumption is",Comsumption,"l per 100 km")