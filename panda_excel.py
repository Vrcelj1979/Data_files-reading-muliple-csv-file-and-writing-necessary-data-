import pandas as pd


# First you nead to install several python package such as a: pandas, virtualenv, openpyxl, xlrd, xlsxwriter, than you can start

# reading excel and csv file
"""
df = pd.read_csv("vozilo1.csv")

print (df)
"""

file = 'Vozila.xls'

xl = pd.ExcelFile(file)

print(xl.sheet_names)

df1 = xl.parse('Sheet2')

for index, row in df1.iterrows():
    print(index, row[5], row['Postanki POI'])


# writer excel file


writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')

df1.to_excel(writer, 'Sheet1')

writer.save()


# writer csv file
"""
df.to_csv("example.csv")
"""

