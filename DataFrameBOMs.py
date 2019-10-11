import pandas as pd
import os
pd.set_option('display.max_columns',20)

# create list of files to import
folder = r"C:\Users\coffmlv\Documents\1_ESD\Inventory Lead Time\BOMs"
filelist = os.listdir(folder)

# call out specific column names to include (ignoring all others)
colNames = ['Obj    ', 'Object description                      ', 'Quantity', 'Un']

list_dfs = []
# loop through and import each file as a dataframe in the list object
for filename in filelist:
    path = os.path.join(folder, filename)
    #print(path)
    list_dfs.append(pd.read_csv(os.path.realpath(path), sep='|', skiprows=9, comment="-", usecols=colNames, encoding='unicode_escape'))

# add the file name as a new column to each dataframe
for dataframe, filename in zip(list_dfs, filelist):
    dataframe['CatItem'] = filename[:-4]

# concatenate each of the dataframes into a large dataframe
testData = pd.concat(list_dfs, ignore_index=True)

#print(testData.head())



