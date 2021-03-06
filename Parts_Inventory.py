import pandas as pd
import DataFrameBOMs as boms
import CatalogTracker as tracker
import P90LeadTimes as leadtime
# pd.set_option('display.width',200)

# boms.bom
# costed.cost
# tracker.catalog


def get_bom(CatItem):
    """returns DataFrame containing part number, part description and qty needed in BOM for a catalog item"""
    df = boms.bom.loc[boms.bom['CatItem'] == CatItem]
    return df


def get_CatalogItems(part):
    """returns DataFrame containing part number, part description and qty needed in BOM for a catalog item"""
    df = boms.bom[boms.bom['PartNumber'] == part]
    return df


def get_productline(CatItem):
    """returns DataFrame containing BOM details, Product Line and current Tracker Status for a catalog item"""
    df_bom = get_bom(CatItem)
    col_merge = ['Product Line', 'SAP Product Number', 'Description', 'BOM Status', 'Cost Roll',
                 'Installation & Operation Manual']
    df_merge = pd.merge(df_bom, tracker.catalog[col_merge], left_on="CatItem", right_on="SAP Product Number", how="left")
    # print(df_merge.columns)
    col_final = ['PartNumber', 'PartDesc', 'BomQty', 'BOMunit', 'CatItem', 'Product Line', 'Description', 'BOM Status',
                 'Cost Roll', 'Installation & Operation Manual']
    df = df_merge[col_final]
    return df


def get_leadCat(CatItem):
    """returns a DataFrame that contains BOM list and associated item cost and lead time"""
    df_pl = get_productline(CatItem)
    col_merge = ['DeletionFlag', 'Material', 'ChangedOn', 'NetPrice', 'Crcy', 'PricingQuantity', 'PricingUnit',
                 'Matl Group', 'MinOrderQty', 'MinOrderUnit', 'PlannedLeadTime']
    df_merge = pd.merge(df_pl, leadtime.lead[col_merge], left_on="PartNumber", right_on="Material", how="left")
    col_final = ['PartNumber', 'PartDesc', 'BomQty', 'BOMunit', 'CatItem', 'Product Line', 'Description', 'BOM Status',
                 'Cost Roll', 'Installation & Operation Manual', 'DeletionFlag', 'ChangedOn', 'NetPrice', 'Crcy',
                 'PlannedLeadTime']
    df = df_merge[col_final]
    return df


def get_leadPart(part, product_line):
    """returns DataFrame that contains lead time and cost for a given list of items assuming one product line
    i.e. - 'USP', 'HI', 'LI', '8RO', '4RO' """

    df_bom_all = get_CatalogItems(part)
    cat_items_df = tracker.catalog[tracker.catalog['Product Line'].str.contains(product_line, na=False)]
    # TODO make more robust using LIKE
    #  tracker.catalog.loc[tracker.catalog['Product Line'] == product_line]

    cat_items = cat_items_df['SAP Product Number'].tolist()
    df_bom = df_bom_all[df_bom_all['CatItem'].isin(cat_items)]

    col = ['DeletionFlag', 'Material', 'ChangedOn', 'NetPrice', 'Crcy', 'PlannedLeadTime']

    df_merge = pd.merge(df_bom, leadtime.lead[col], left_on="PartNumber", right_on="Material", how="left")

    return df_merge


def get_partslist(CatItem, LeadTimes, mfg_time=None):
    """ pulls a list of parts whose lead time is greater than allotted for current goal for a given catalog item
            lead time is a list of options, catalog items are a list

            returns part_cost, part_list:
                part_cost { CatalogItem : { Proposed Lead Time : Inventory Cost } , Cat... }
                part_list { CatalogItem : { Proposed Lead Time : [ List of Parts] } , Cat... }"""
    parts_list = {}
    parts_cost = {}

    mfg_time = mfg_time or 15  # in work days

    for item in CatItem:
        df_lead = get_leadCat(item)
        dict_key = item

        for time in LeadTimes:
            lead_days = time * 5  # time is in weeks, convert to work days
            order_time = lead_days - mfg_time
            item_parts = []
            item_cost = 0.0

            for part in df_lead.itertuples():
                if part.PlannedLeadTime >= order_time:
                    item_parts.append(part.PartNumber)
                    # format string NetPrice
                    price = part.NetPrice

                    item_cost += float(part.BomQty) * price

            if len(item_parts) == 0:
                pass
            else:
                parts_list[(dict_key, time)] = item_parts
                parts_cost[(dict_key, time)] = item_cost

    df_cost = pd.DataFrame.from_dict(parts_cost, orient='index', columns=['Inv_Cost']).fillna(0)
    s_list = pd.Series(parts_list)
    df_list = s_list.to_frame()
    df_list.columns = ['Inv_Parts']

    df_cost.index = pd.MultiIndex.from_tuples(df_cost.index, names=('CatalogItem','LeadTime'))
    df_list.index.names = ['CatalogItem', 'LeadTime']

    return df_cost, df_list


if __name__ =="__main__":
    testLeads = [3, 4, 8, 10, 12]  # weeks lead time
    testItems = ['USP-120AS50.88', 'USP-136AS50.88', 'USP-230AS50.88', '011-SLDFVLEX.88']
    # cost, items = get_partslist(testItems, testLeads)
    # print(cost, '\n')
    # print(items.loc['USP-120AS50.88'])

    testItem = 'USP-120AS50.88'
    # print(get_leadCat(testItem).head())

    part = 'PTS1001'
    # print(get_leadPart(part, 'USP'))
