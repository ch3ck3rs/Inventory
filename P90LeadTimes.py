import pandas as pd
from Strip import strip_obj
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 200)

path = r"C:\Users\coffmlv\Documents\1_ESD\Inventory Lead Time\Plant 90 Leadtimes - 10.24.19.csv"

lead_all = pd.read_csv(path)
lead_all.dropna(how='all')

lead_notnull = lead_all[pd.notnull(lead_all.iloc[:,4])]

NewColNames = {'D':'DeletionFlag', 'Changed On':'ChangedOn', 'Per':'PricingQuantity', 'OPU':'PricingUnit', 'Order Quantity':'MinOrderQty',
               'OUn':'MinOrderUnit', 'Net Price':'NetPrice', 'PTm':'PlannedLeadTime'}

lead_multi = lead_notnull.apply(strip_obj, axis=0)
lead_multi = lead_multi.rename(NewColNames, axis=1)
lead_multi.ChangedOn = pd.to_datetime(lead_multi.ChangedOn)

lead_sort = lead_multi.sort_values('ChangedOn')

lead = lead_sort.drop_duplicates(['Material'], keep='last')

# lead = lead_sort.loc[lead_sort['Material'].str.contains('PTS1160')]
# lead = lead.loc[lead['Material'].str.contains('PTS1160', na=False)]

# print(lead_all.columns)

# print(lead.sample(20))