import pandas as pd
from Strip import strip_obj
# pd.set_option('display.max_columns', 50)
# pd.set_option('display.width', 150)


path = r"C:\Users\coffmlv\Documents\1_ESD\Catalog\PTS Equip Standardization Tracker.xlsx"

list = pd.read_excel(path, sheet_name=None, skiprows=3, comment="COUNT")

key = list.keys()

col = ['Product Line', 'SAP Product Number', 'Description', 'Mechanical Drawings',
       'Electical Drawings', 'BOM Status', 'Software', 'QC Work Instructions', 'Cost Roll',
       'SAP P/N Status', 'Installation & Operation Manual',
       'Quick Start Guide', 'Spec Sheet', 'Brochure',
       'Outline Agreements & Costs in SAP']

sheet_ban = ['SUMMARY', '4" RO Axeon', '8" RO XLX']

for item in sheet_ban:
    list.pop(item)

for sheet in list.keys():
    #print(sheet)
    list[sheet].dropna(how='all')
    list[sheet] = list[sheet][pd.notnull(list[sheet].iloc[:,2])]
    list[sheet] = list[sheet][col]
    #print(list[sheet]. head())

Init_Catalog = pd.concat(list, ignore_index=True, sort=False)

catalog = Init_Catalog.filter(items=['Product Line', 'SAP Product Number', 'Description', 'Mechanical Drawings',
       'Electical Drawings', 'BOM Status', 'Software', 'QC Work Instructions', 'Cost Roll',
       'SAP P/N Status', 'Installation & Operation Manual',
       'Quick Start Guide', 'Spec Sheet', 'Brochure',
       'Outline Agreements & Costs in SAP'])

catalog = catalog.apply(strip_obj, axis=0)

dropped = []

for row in catalog.itertuples():

    part = row._2

    if part.startswith('PTS'):
        new_part = part.split(' / ')[1]
        catalog.at[row.Index, 'SAP Product Number'] = new_part

    elif '011' not in part and 'USP' not in part:
        dropped.append(part)
        catalog.drop(row.Index, inplace=True)


# catalog.to_csv(r"C:\Users\coffmlv\Documents\1_ESD\Catalog\Tracker.csv")
# print(catalog.columns)
# print(catalog.sample(15))
# line = catalog['Product Line'].tolist()
# print(set(line))
# prod = catalog['SAP Product Number'].tolist()
# print(prod)
# print(dropped)
