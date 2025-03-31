import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('housing.csv')

longitude = df['longitude']
latitude = df['latitude']
median_house_value = df['median_house_value']





plt.scatter(longitude, latitude, c=median_house_value)

plt.scatter(-118.2426, 34.0549, color='black', label='Los Angeles', s=1000, marker='*')
plt.scatter(-122.4194, 37.7749, color='black', label='San Francisco', s=1000, marker='*')

plt.colorbar(label="Median House Value")
plt.xlabel("Longitude", fontsize=20)
plt.ylabel("Latitude", fontsize=20)
plt.title("Median House Values in California (1990)", fontsize=36)
plt.show()