import pandas as pd
import os

path = r"C:\Users\coffmlv\Documents\1_ESD\Inventory Lead Time\BOMs\011-CLSFFDA.88.txt"

colNames = ['Obj    ', 'Object description                      ', 'Quantity', 'Un']

testData = pd.read_csv(path, sep='|', skiprows=9, comment="-", usecols=colNames)
testData['CatItem'] = os.path.basename(path[:-4])

print(testData.head())



