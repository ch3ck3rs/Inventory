from InventoryParts import *
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 150)


def get_HighLevel(ProductLine):
    """returns the High Level Product Line in a list ['USP', 'RO', ...] """
    line = []
    for item in ProductLine:
        if pd.isna(item):
            pass
        else:
            if item not in line:
                line.append(item)
    return line


def get_products(ProductLine):
    """returns list of products for a given product line"""
    products = tracker.catalog[tracker.catalog['Product Line'].str.contains(ProductLine, na=False)]
            # TODO make more robust using LIKE
             # original line >> tracker.catalog[tracker.catalog['Product Line'] == ProductLine]
    products = products['SAP Product Number'].tolist()
    return products


def get_common(ProductList):
    """Given a list of products, returns dataframes for all, most, everything.
    Most is defined as 25% of catalog items or 5 items, which ever is larger"""

    part_dict = {}

    list_len = len(ProductList)
    quarter = list_len/4

    if quarter >= 5:
        most = 0.75
    else:
        most = 5/list_len

    for item in ProductList:
        bom = get_bom(item)

        for part in bom.PartNumber:
            line = bom.loc[bom['PartNumber'] == part]
            bom_qty = line.iloc[0]['BomQty']
            adder = [1.0, bom_qty]

            if part in part_dict.keys():
                current = part_dict[part]
                new_part = [sum(i) for i in zip(adder, current)]
                part_dict[part] = new_part

            else:
                part_dict[part] = adder

    df = pd.DataFrame.from_dict(part_dict, orient='index')
    df['Part'] = df.index
    df_everything = df.reset_index(drop=True)
    df_everything.columns = ["Appearances", "Total_Qty", "Part"]

    df_everything['Percent_of_BOMs'] = df_everything.Appearances / list_len

    df_all = df_everything.loc[df_everything['Percent_of_BOMs'] == 1.0]

    df_most = df_everything.loc[df_everything['Percent_of_BOMs'] >= most]

    return df_all, df_most, df_everything





CatItems = tracker.catalog['SAP Product Number']
df_parts = tracker.catalog[['Product Line', 'SAP Product Number']]
product_list = get_products("USP")
testItem = ['USP-120AS50.88', 'USP-130AS25.88']
testItem2 = ['USP-120AS50.88', 'USP-120AS25.88', 'USP-130AS50.88', 'USP-130AS25.88', 'USP-136AS50.88', 'USP-136AS25.88', 'USP-230AS50.88', 'USP-330AS50.88', 'USP-430AS50.88', 'USP-630AS50.88', 'USP-830AS50.88']

all, most, everything = get_common(product_list)

# print(all.describe(), '\n', most.describe(), '\n', everything.describe())
# print(all.sample(5), '\n', most.sample(5), '\n', everything.sample(5))

