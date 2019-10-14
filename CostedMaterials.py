import pandas as pd
pd.set_option('display.max_columns',20)

path = r"C:\Users\coffmlv\Documents\1_ESD\Costing\ZCOST_ACC.xlsx"

Costed = pd.read_excel(path, sheet_name="Plnt90")
Costed.dropna(how='all')


# print(Costed.sample(10))