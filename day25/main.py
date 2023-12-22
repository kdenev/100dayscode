# output = list()

# with open("day25\weather_data.csv", "r") as data:
#     for line in data.readlines():
#         output.append(line.strip())

# print(output)

# import csv

# with open("day25\weather_data.csv", "r") as data:
#     data = csv.reader(data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#             # print(row)

# print(temperatures)

import pandas as pd

data = pd.read_csv("day25\weather_data.csv")
# print(data)

# data_dict = data.to_dict()
# print(data_dict)
print(data['temp'].mean())
print(data['temp'].max())
print(data[data['temp'] == data['temp'].max()])
monday_temp = data[data['day'] == 'Monday']['temp'].values[0]
print(monday_temp*9/5 + 32)

