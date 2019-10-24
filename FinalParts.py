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


def get_final(product_line, percentage=None):
    """Product Lines are
        ['4" RO', '8" RO', 'LI CF', 'LI DEALK', 'LI IF', 'LI MMF', 'LI SOFT', 'USP']
        Choose 1 for that specific line, or ['RO', 'HI', 'LI', 'USP'] for category

        percentage determines the % of BOMs an item must show up in for the percentage of BOMs dataframe.
        default is 75%

        Returns list of df = [ parts common to all BOMs, parts common to percentage of BOMs, parts in every BOM]"""

    final_list = []
    percentage = percentage or .75

    product_list = get_products(product_line)
    common_products, num_of_products, percent_used = get_common(product_list, percentage)

    col = ['Part', 'description', 'Appearances', 'Total_Qty', 'Percent_of_BOMs', 'lead', 'price',
           'qty_max', 'qty_min', 'qty_avg']

    # check for empty dataframes and then merge

    for df in common_products:
        if len(df.index) == 0:
            df.append({"Part":"No Values Returned"}, ignore_index=True)
            final_list.append(df)
        else:
            list_parts = df['Part'].values

            merged_df = pd.merge(df, get_Inventory(list_parts, product_line),
                                 right_on="part",  left_on="Part", how="left")
            final_list.append(merged_df[col])

    return final_list, num_of_products, percent_used


final, num, percent = get_final('LI', percentage=0.2)

# print("_",num,"_ catalog items are being considered")
# print("_",percent,"_ percentage used to calculate the MOST graph")
# print("_",len(final[2]['Part'].tolist()),"_ parts considered")
#
# for df in final:
#     if len(df.index) == 0:
#         print('\nNo Items Returned \n')
#     else:
#         print(df.head(), '\n')
