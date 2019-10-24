import pandas as pd
import os
from Strip import strip_obj
# pd.set_option('display.max_columns', 50)
# pd.set_option('display.width', 200)

path = r"C:\Users\coffmlv\Documents\1_ESD\Inventory Lead Time\Plant 90 Leadtimes - 10.9.19.txt"
colNames = ['Purch.Doc.', 'D', 'Plnt', 'Vendor', 'Material', 'Short Text', 'Changed On', 'Net Price',
            'Crcy', 'Per', 'OPU', 'Matl Group', 'Order Quantity', 'OUn', 'Gross value', 'P', 'OA Target Value', 'PTm']

lead_all = pd.read_csv(os.path.realpath(path), sep='|', comment="-", encoding='unicode_escape')
lead_all = lead_all.rename(columns=lambda x: x.strip())
lead_all.dropna(how='all')
lead_notnull = lead_all[pd.notnull(lead_all.iloc[:,6])]
lead_multi = lead_notnull[colNames]
lead_multi = lead_multi.apply(strip_obj, axis=0)

NewColNames = {'D':'DeletionFlag', 'Changed On':'ChangedOn', 'Per':'PricingQuantity', 'OPU':'PricingUnit', 'Order Quantity':'MinOrderQty',
               'OUn':'MinOrderUnit', 'Net Price':'NetPrice', 'PTm':'PlannedLeadTime'}

lead_multi = lead_multi.rename(NewColNames, axis=1)

lead_multi.ChangedOn = pd.to_datetime(lead_multi.ChangedOn)
lead = lead_multi.sort_values('ChangedOn').drop_duplicates(['Material'], keep='last')

# lead = lead.loc[lead['Material'] == 'PTS1001']

# print(lead.columns)

# print(lead.head(20))