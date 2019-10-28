import pandas as pd
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import DataFrameBOMs as boms
import P90LeadTimes as leadtime
from FinalParts import *
import CatalogTracker as tracker

pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 200)

df_bom1 = boms.bom
df_bom = df_bom1.drop_duplicates(subset='PartNumber')
df_lead = leadtime.lead

###

# usp_df = tracker.catalog[tracker.catalog[['Product Line'] == 'USP']]
# usp = usp_df['SAP Product Number'].tolist()

###

df_merge = pd.merge(df_bom, df_lead, right_on='Material', left_on='PartNumber', how='left')
df_merge1 = pd.merge(df_bom1, df_lead, right_on='Material', left_on='PartNumber', how='left')

df_null = df_merge.loc[pd.isnull(df_merge['PlannedLeadTime'])]

df_not = df_merge.loc[pd.isnull(df_merge['Purch.Doc.'])]

df_all_null = df_merge1.loc[pd.isnull(df_merge1['PlannedLeadTime'])]

###

col = ['PartNumber', 'PartDesc', 'BomQty', 'BOMunit', 'CatItem', 'Purch.Doc.', 'DeletionFlag', 'Plnt', 'Vendor',
       'ChangedOn', 'NetPrice', 'Crcy', 'Matl Group', 'PlannedLeadTime']

col_null = ['PartNumber', 'PartDesc', 'Purch.Doc.', 'DeletionFlag', 'Plnt', 'Vendor',
       'ChangedOn', 'NetPrice', 'Crcy', 'Matl Group', 'PlannedLeadTime']

###
# print files to an excel sheet

path = r'C:\Users\coffmlv\Documents\1_ESD\Inventory Lead Time\Results\Catalog_parts_not_setup.xlsx'
writer = pd.ExcelWriter(path)

df_merge[col].to_excel(writer, sheet_name='All Catalog Parts')
df_null[col_null].to_excel(writer, sheet_name='Parts with no Lead')
df_not[col_null].to_excel(writer, sheet_name='Parts not setup')
df_all_null[col].to_excel(writer, sheet_name='Dup Parts with no Lead')

writer.save()

###
# graphs

# df_app = df_merge1.loc[df_merge1['CatItem'].str.contains('USP')]
#
# final, num, percent = get_final('USP')
#
# df = final[2]
#
# # df_graph = pd.merge(df_app, df, left_on='PartNumber')
#
# # print(df_app.sample(10))
# g = sns.pairplot(df, x_vars=['lead'],y_vars=['Appearances', 'qty_avg'])
