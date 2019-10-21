import pandas as pd
from Strip import strip_obj
pd.set_option('display.max_columns',50)
pd.set_option('display.width',150)

mfg_time = pd.read_csv(r"C:\Users\coffmlv\Documents\1_ESD\Catalog\P90MFGTimes.csv").apply(strip_obj, axis=0)

# print(mfg_time.head())