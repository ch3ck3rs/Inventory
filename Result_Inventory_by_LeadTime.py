import pandas as pd
from InventoryParts import get_partslist
import CatalogTracker as tracker


LeadTimes = [6, 8, 10, 12]
product_line = '8" RO'
mfg_time = 30  # change in InventoryParts.py line 87

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

summary = pd.DataFrame({'Title':['Product Line', 'Number of Products Considered', 'Lead Times Considered', 'MFG Time'],
                        'Value':[product_line, num, LeadTimes, mfg_time]})

path = r'C:\Users\coffmlv\Documents\1_ESD\Inventory Lead Time\Results\LeadTime_Parts_8RO_20mfgDays.xlsx'
writer = pd.ExcelWriter(path)

summary.to_excel(writer, sheet_name='SUMMARY')
df_cost.to_excel(writer, sheet_name='Cost to Inventory')
df_list.to_excel(writer, sheet_name='Parts to Inventory')
CatItems_df['SAP Product Number'].to_excel(writer, sheet_name='Catalog Considered')

writer.save()
