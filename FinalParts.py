from CommonParts import *
from InventoryParts import *
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 250)


def get_Inventory(part_list, line):
    """Given list of part number and a prodcuct line,
    return description, lead time, price and qty stats """
    dict_inv = {}
    for part in part_list:
        df_lead = get_leadPart(part, line)
        qty = df_lead['BomQty'].tolist()
        dict_part = {'part':part,
                     'description':df_lead['PartDesc'].max(),
                     'lead':df_lead['PlannedLeadTime'].max(),
                     'price':df_lead['NetPrice'].max(),
                     'qty_min':min(qty),
                     'qty_max':max(qty),
                     'qty_avg':sum(qty)/(1+len(qty))}

        dict_inv[part] = dict_part

    df_dict = pd.DataFrame.from_dict(dict_inv).transpose()
    df = df_dict.reset_index(drop=True)

    return df

###


def get_final(product_line):
    """Product Lines are
        ['4" RO', '8" RO', 'LI CF', 'LI DEALK', 'LI IF', 'LI MMF', 'LI SOFT', 'USP']

        Choose 1 for that specific line, or ['RO', 'HI', 'LI', 'USP'] for category"""

    product_list = get_products(product_line)
    all_f, most_f, everything_f = get_common(product_list)

    # check for empty dataframes
    #if len(all_f.index) ==0:


    list_parts_all = all_f['Part'].values
    list_parts_most = most_f['Part'].values
    list_parts_everything = everything_f['Part'].values

    col = ['Part', 'description', 'Appearances', 'Total_Qty', 'Percent_of_BOMs', 'lead', 'price',
           'qty_max', 'qty_min', 'qty_avg']

    all1 = pd.merge(all_f, get_Inventory(list_parts_all, product_line), right_on="part",  left_on="Part", how="left")
    # TODO getting key error on 'part' for LI but not for USP.
    most1 = pd.merge(most_f, get_Inventory(list_parts_most, product_line), right_on="part",  left_on="Part", how="left")
    everything1 = pd.merge(everything_f, get_Inventory(list_parts_everything, product_line), right_on="part",  left_on="Part", how="left")

    return all1[col], most1[col], everything1[col]


# all, most, everything = get_final("LI")

# print(all.sample(10), '\n')
# print(most.sample(10), '\n')
# print(everything.sample(10))
