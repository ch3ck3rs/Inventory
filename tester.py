import pandas
import matplotlib.pyplot as plt
from CommonParts import *
from PlotLabel import *
from PartsToInventory import *
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 250)

###

product_list = get_products("USP")
all, most, everything = get_common(product_list)

###

list_parts_all = all['Part'].values
list_parts_most = most['Part'].values
list_parts_everything = everything['Part'].values

# print(list_parts_all)

###
def get_Inventory(list, line):
    dict = {}
    for part in list:
        dict_part = {}
        df_lead = get_leadPart(part, line)
        qty = df_lead['BomQty'].tolist()
        dict_part = {'part':part,
                     'description':df_lead['PartDesc'].max(),
                     'lead':df_lead['PlannedLeadTime'].max(),
                     'price':df_lead['NetPrice'].max(),
                     'qty_min':min(qty),
                     'qty_max':max(qty),
                     'qty_avg':sum(qty)/(1+len(qty))}

        dict[part] = dict_part

    df_dict = pd.DataFrame.from_dict(dict).transpose()
    df = df_dict.reset_index(drop=True)

    return df

###


def get_final(product_line):
    product_list = get_products(product_line)
    all, most, everything = get_common(product_list)

    list_parts_all = all['Part'].values
    list_parts_most = most['Part'].values
    list_parts_everything = everything['Part'].values

    col = ['Part', 'description', 'Appearances', 'Total_Qty', 'Percent_of_BOMs', 'lead', 'price',
           'qty_max', 'qty_min', 'qty_avg']

    all1 = pd.merge(all, get_Inventory(list_parts_all, product_line), right_on="part",  left_on="Part", how="left")
    most1 = pd.merge(most, get_Inventory(list_parts_most, product_line), right_on="part",  left_on="Part", how="left")
    everything1 = pd.merge(everything, get_Inventory(list_parts_everything, product_line), right_on="part",  left_on="Part", how="left")

    return all1[col], most1[col], everything1[col]

# print(get_Inventory(list_parts_all).sample(10))
# print(all)


all, most, everything = get_final("USP")

print(all.sample(10), '\n')
print(most.sample(10), '\n')
print(everything.sample(10))