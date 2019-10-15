import pandas as pd
import DataFrameBOMs as boms
import CostedMaterials as costed
import CatalogTracker as tracker
import P90LeadTimes as leadtime
pd.set_option('display.width',200)


# boms.bom
# costed.cost
# tracker.catalog


def get_bom(CatItem):
    """returns DataFrame containing part number, part description and qty needed in BOM for a catalog item"""
    df = boms.bom.loc[boms.bom['CatItem'] == CatItem]
    return df

def get_productline(CatItem):
    """returns DataFrame containing BOM details, Product Line and current Tracker Status for a catalog item"""
    df_bom = get_bom(CatItem)
    col_merge = ['Product Line', 'SAP Product Number', 'Description', 'BOM Status', 'Cost Roll',
                 'Installation & Operation Manual']
    df_merge = pd.merge(df_bom, tracker.catalog[col_merge], left_on="CatItem", right_on="SAP Product Number", how="left")
    #print(df_merge.columns)
    col_final = ['PartNumber', 'PartDesc', 'BomQty', 'BOMunit', 'CatItem', 'Product Line', 'Description', 'BOM Status',
                 'Cost Roll', 'Installation & Operation Manual']
    df = df_merge[col_final]
    return df


def get_lead(CatItem):
    """returns a DataFrame that contains BOM list and associated item cost and lead time"""
    df_pl = get_productline(CatItem)
    col_merge = ['DeletionFlag', 'Material', 'Changed On', 'Net Price', 'Crcy', 'PricingQuantity', 'PricingUnit',
                 'Matl Group', 'MinOrderQty', 'MinOrderUnit', 'PlannedLeadTime']
    df_merge = pd.merge(df_pl, leadtime.lead[col_merge], left_on="PartNumber", right_on="Material", how="left")
    col_final = ['PartNumber', 'PartDesc', 'BomQty', 'BOMunit', 'CatItem', 'Product Line', 'Description', 'BOM Status',
                 'Cost Roll', 'Installation & Operation Manual', 'DeletionFlag', 'Changed On', 'PlannedLeadTime']
    df = df_merge[col_final]
    return df


def get_partslist(CatItem, LeadTimes):
    """ pulls a list of parts whose lead time is greater than allotted for current goal for a given catalog item
            lead time is a list of options, catalog items are a list"""
    parts_list = {}

    for item in CatItem:
        df_lead = get_lead(item)
        dict_key = item
        dict_value = {}

        for time in LeadTimes:
            lead_days = time * 5  # time is in weeks, convert to work days
            mfg_time = 10  # in work days
            order_time = lead_days - mfg_time
            item_value = []

            for part in df_lead.itertuples():
                if part.PlannedLeadTime >= order_time:
                    item_value.append(part.PartNumber)

            if len(item_value) == 0:
                pass
            else:
                dict_value[time] = item_value

        if len(dict_value) == 0:
            pass
        else:
            parts_list[dict_key] = dict_value

    return parts_list


testLeads = [6, 8, 10, 12]  # weeks lead time
testItems = ['USP-120AS50.88', 'USP-136AS50.88', 'USP-230AS50.88', '011-SLDFVLEX.88']
# print(get_partslist(testItems, testLeads))
