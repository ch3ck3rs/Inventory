import pandas as pd
import numpy as np
import os
from Strip import strip_obj
pd.set_option('display.max_columns', 20)

# Data source SAP t-code CS11 plant 90

# create list of files to import
folder = r"C:\Users\coffmlv\Documents\1_ESD\Inventory Lead Time\BOMs"
filelist = os.listdir(folder)

# call out specific column names to include (ignoring all others)
colNames = ['Component number', 'Object description', 'Comp. Qty (CUn)', 'Un']

list_dfs = []
# loop through and import each file as a dataframe in the list object
for filename in filelist:
    path = os.path.join(folder, filename)
    list_dfs.append(pd.read_csv(os.path.realpath(path), usecols=colNames))

# add the file name as a new column to each dataframe
for dataframe, filename in zip(list_dfs, filelist):
    dataframe['CatItem'] = filename[:-4]

# concatenate each of the dataframes into a large dataframe
bom = pd.concat(list_dfs, ignore_index=True)
bom = bom.apply(strip_obj, axis=0)

NewColNames = {'Component number':'PartNumber', 'Object description':'PartDesc', 'Comp. Qty (CUn)':'BomQty', 'Un':'BOMunit'}

bom = bom.rename(NewColNames, axis=1)
# bom['BomQty'] = pd.to_numeric(bom.BomQty)
# bom['BomQty'] = bom.BomQty.fillna(0.0)


# print(bom.columns)
# print(bom.sample(20))
# print(bom[bom['PartNumber'].str.contains('PTS1419')])
# print(bom['BomQty'].describe())
