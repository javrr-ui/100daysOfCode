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
#
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# avg_temp = "{:.2f}".format(data["temp"].mean())
# print(f"Average temperature is: {avg_temp}")
# print(f"Maximum temperature is: {data['temp'].max()}")
#
# # Get data in a row
# print(data[data["day"] == "Monday"])
#
# # Get row with max temperature
# print(data[data["temp"] == data["temp"].max()])
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

count = data["Primary Fur Color"].value_counts()

data_dict = {
    "Fur color": ["gray", "red", "black"],
    "count": [count["Gray"], count["Cinnamon"], count["Black"]]
}

