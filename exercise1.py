# Read data from a excel or csv file
# import pandas module for use
import pandas as pd
from pandas import ExcelWriter

# Read csv or xls as data frame
df = pd.read_csv("ConsumerComplaints.csv", low_memory=False)

print(df.shape)  # size of the data

print((df.dtypes))  # data types

print(df.columns)  # column names

df = df[["Product", "Sub-product"]]  # pick columns for the dataframe

product_name = df.groupby("Product")

df = product_name.sum()

print(df)

# save to new CSV file
df.to_csv('products.csv', encoding='utf-8')

# save to xls

writer = ExcelWriter('products.xlsx')
df.to_excel(writer, 'Sheet1')
writer.save()
