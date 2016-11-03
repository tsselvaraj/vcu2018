# Read data from a excel or csv file
# import pandas module for use
import pandas as pd
from pandas import ExcelWriter

# Read csv or xls as data frame
df = pd.read_csv("Crimes2012-2015.csv", low_memory=False)

print(df.shape)  # size of the data

print((df.dtypes))  # data types

print(df.columns)  # column names

df = df[["DATE.OCC", "TIME.OCC"]]  # pick columns for the dataframe

print(df.describe())

# Process, Analysis




# save to new CSV file
# df.to_csv('city.csv', encoding='utf-8')

# save to xls

# writer = ExcelWriter('city.xlsx')
# df.to_excel(writer,'Sheet1')
# writer.save()
