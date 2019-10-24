import pandas as pd
from Strip import strip_obj
# pd.set_option('display.max_columns',50)
# pd.set_option('display.width',200)

path = r"C:\Users\coffmlv\Documents\1_ESD\Costing\ZCOST_ACC.xlsx"

cost = pd.read_excel(path, sheet_name="Plnt90").rename(columns=lambda x: x.strip())
cost.dropna(how='all')
cost = cost.apply(strip_obj, axis=0)


# print(cost.sample(10))