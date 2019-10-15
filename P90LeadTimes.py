import pandas as pd
import os
from Strip import strip_obj
pd.set_option('display.max_columns',50)
pd.set_option('display.width',200)

path = r"C:\Users\coffmlv\Documents\1_ESD\Inventory Lead Time\Plant 90 Leadtimes - 10.9.19.txt"
colNames = ['Purch.Doc.', 'D', 'Plnt', 'Vendor', 'Material', 'Short Text', 'Changed On', 'Net Price',
            'Crcy', 'Per', 'OPU', 'Matl Group', 'Order Quantity', 'OUn', 'Gross value', 'P', 'OA Target Value', 'PTm']

lead_all = pd.read_csv(os.path.realpath(path), sep='|', comment="-", encoding='unicode_escape')
lead_all = lead_all.rename(columns=lambda x: x.strip())
lead_all.dropna(how='all')
lead_notnull = lead_all[pd.notnull(lead_all.iloc[:,6])]
lead = lead_notnull[colNames]
lead = lead.apply(strip_obj, axis=0)

NewColNames = {'D':'DeletionFlag', 'Per':'PricingQuantity', 'OPU':'PricingUnit', 'Order Quantity':'MinOrderQty',
               'OUn':'MinOrderUnit', 'PTm':'PlannedLeadTime'}

lead = lead.rename(NewColNames, axis=1)

# print(lead.columns)
# print(lead.head(20))