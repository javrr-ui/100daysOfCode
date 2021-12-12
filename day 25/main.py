# with open("weather_data.csv") as file:
#     data = list(map(str.strip, file.readlines()))

# import csv
#
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = [row[1] for row in data]
#     temperatures.__delitem__(0)
#     temperatures = [int(temp) for temp in temperatures]
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
print(temp_list)

avg_temp = "{:.2f}".format(data["temp"].mean())
print(f"Average temperature is: {avg_temp}")
print(f"Maximum temperature is: {data['temp'].max()}")
