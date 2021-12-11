# with open("weather_data.csv") as file:
#     data = list(map(str.strip, file.readlines()))

import csv

with open("weather_data.csv") as weather_file:
    data = csv.reader(weather_file)
    for row in data:
        print(row)