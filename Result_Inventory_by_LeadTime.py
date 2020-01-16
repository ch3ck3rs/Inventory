import pandas as pd
from Parts_Inventory import get_partslist
import CatalogTracker as tracker
from datetime import datetime
import os


LeadTimes = [3, 4, 5, 6, 8, 10, 12]
product_line = 'USP'
mfg_time = 15  # change in Parts_Inventory.py line 87

###
# for all inventory, use CatItems_all in get_partslist() below.
# for a specific product line, use CatItems in get_partslist() below.

CatItems_all = tracker.catalog['SAP Product Number']

CatItems_df = tracker.catalog[tracker.catalog['Product Line'].str.contains(product_line, na=False)]
CatItems = CatItems_df['SAP Product Number'].tolist()

###

df_cost, df_list = get_partslist(CatItems, LeadTimes)
num = len(CatItems)

###
# sumarize data and put into excel. Change the file name in path below

now = datetime.now()
stamp = now.strftime("%m-%d-%y_%H-%M")

summary = pd.DataFrame({'Title':['Product Line', 'Number of Products Considered', 'Lead Times Considered', 'MFG Time'],
                        'Value':[product_line, num, LeadTimes, mfg_time]})


path = r"C:\Users\coffmlv\Documents\1_ESD\Inventory Lead Time\Results"
base_name = "LeadTime_Parts_USP_"+str(mfg_time)+"mfgDays"+stamp+".xlsx"
writer = pd.ExcelWriter(os.path.join(path, base_name))

summary.to_excel(writer, sheet_name='SUMMARY')
df_cost.to_excel(writer, sheet_name='Cost to Inventory')
df_list.to_excel(writer, sheet_name='Parts to Inventory')
CatItems_df['SAP Product Number'].to_excel(writer, sheet_name='Catalog Considered')

writer.save()
