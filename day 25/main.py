# with open("weather_data.csv") as file:
#     data = list(map(str.strip, file.readlines()))

import csv

with open("weather_data.csv") as weather_file:
    data = csv.reader(weather_file)
    temperatures = [row[1] for row in data]
    temperatures.__delitem__(0)
    temperatures = [int(temp) for temp in temperatures]
    print(temperatures)
