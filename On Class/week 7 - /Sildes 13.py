import pandas as pd
import matplotlib.pyplot as plt
# Example data
data = {
'Temperature': [22, 23, 21, 20, 19, 18, 17, 16, 15, 14],
'Movement': [1, 0, 1, 1, 0, 0, 1, 0, 1, 1]
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