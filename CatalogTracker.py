import pandas as pd
pd.set_option('display.max_columns',20)

path = r"C:\Users\coffmlv\Documents\1_ESD\PTS Equip Standardization Tracker.xlsx"

list = pd.read_excel(path, sheet_name="USP",skiprows=3, comment="COUNT")
list.dropna(how='all')

list = list[pd.notnull(list.iloc[:,2])]

print(list.tail())