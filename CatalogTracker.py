import pandas as pd
pd.set_option('display.max_columns',20)

path = r"C:\Users\coffmlv\Documents\1_ESD\PTS Equip Standardization Tracker.xlsx"


list = pd.read_excel(path, sheet_name=None, skiprows=3, comment="COUNT")

key = []
col = ['Product Line', 'SAP Product Number', 'Description', 'Mechanical Drawings',
       'Electical Drawings', 'BOM Status', 'Software', 'QC Work Instructions', 'Cost Roll',
       'SAP P/N Status', 'Installation & Operation Manual',
       'Quick Start Guide', 'Spec Sheet', 'Brochure',
       'Outline Agreements & Costs in SAP']

for item in list.keys():
    if item == "SUMMARY":
        pass
    else:
        key.append(item)
#print(key)


for sheet in key:
    #print(sheet)
    list[sheet].dropna(how='all')
    list[sheet] = list[sheet][pd.notnull(list[sheet].iloc[:,2])]
    list[sheet] = list[sheet][col]
    #print(list[sheet].head())

MidCatalog = pd.concat(list, ignore_index=True, sort=False)

Catalog = MidCatalog.filter(items=['Product Line', 'SAP Product Number', 'Description', 'Mechanical Drawings',
       'Electical Drawings', 'BOM Status', 'Software', 'QC Work Instructions', 'Cost Roll',
       'SAP P/N Status', 'Installation & Operation Manual',
       'Quick Start Guide', 'Spec Sheet', 'Brochure',
       'Outline Agreements & Costs in SAP'])

#print(Catalog.columns)
#print(Catalog.head())