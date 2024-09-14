import csv
import pandas

data = pandas.read_csv("Squirrel.csv")
dic_data = data.to_dict()
print(data["Primary Fur Color"].value_counts())
