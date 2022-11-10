import pandas as pd

xl = pd.ExcelFile("test.xlsx")
df = xl.parse("Sheet1")
df = df.sort_values(by="Value")

writer = pd.ExcelWriter('test.xlsx')
df.to_excel(writer, sheet_name='Sheet1', columns=["Value"], index=False)
writer.save()
