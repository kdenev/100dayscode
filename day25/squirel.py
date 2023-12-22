import pandas as pd

df = pd.read_csv(r"day25\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
output = df['Primary Fur Color'].value_counts().reset_index()

output.to_csv(r"day25\squirrel_coutn.csv", index=False)