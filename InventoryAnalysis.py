import pandas as pd
from PartsToInventory import get_partslist
import CatalogTracker as tracker

LeadTimesFile = pd.read_csv(r"C:\Users\coffmlv\Documents\1_ESD\Inventory Lead Time\LeadTimes")
LeadTimes = LeadTimesFile['LeadTime'].tolist()

CatItems = tracker.catalog['SAP Product Number']

dict_cost, dict_list = get_partslist(CatItems, LeadTimes)

df_cost = pd.DataFrame.from_dict(dict_cost, orient='index').fillna(0)

# print(df_cost.head())