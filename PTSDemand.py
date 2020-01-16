import pandas as pd


path = r"C:\Users\coffmlv\Documents\1_ESD\Inventory Lead Time\GlenwoodProduction_clean.xlsx"

def get_8ROdemand():

    col = ['Nalco Part Number', 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 'Total']
    col_rename = {'Nalco Part Number':'Catalog_item'}

    demand_all = pd.read_excel(path, sheet_name="Summary 8 RO", skiprows=1)
    demand_all.dropna(how="all")
    demand_notnull = demand_all[pd.notnull(demand_all.iloc[:,1])]
    demand_noDel = demand_notnull[~demand_notnull.Recommendation.str.contains("Delete")]
    demand = demand_noDel[col]

    # rename columns
    demand = demand.rename(col_rename, axis=1)

    # group by SAP Number
    demand_group = demand.groupby('Catalog_item').agg({2010:['sum'], 2011:['sum'], 2012:['sum'], 2013:['sum'], 2014:['sum'],
                                                 2015:['sum'], 2016:['sum'], 2017:['sum'], 2018:['sum'], 'Total':['sum']})
    demand_group['Catalog_Item'] = demand_group.index

    # reset index
    demand = demand_group.reset_index(drop=True)

    # add average demand per year
    years = len(demand.columns) - 1
    demand['avg_demand'] = demand['Total'] / years
    demand['100_percent'] = round(demand.avg_demand)
    demand['80_percent'] = round(demand.avg_demand * 0.8)
    demand['60_percent'] = round(demand.avg_demand * 0.6)
    demand['40_percent'] = round(demand.avg_demand * 0.4)
    demand['20_percent'] = round(demand.avg_demand * 0.2)
    demand['vessel_size'] = demand.Catalog_Item.str[5:7]
    demand['vessel_qty'] = demand.Catalog_Item.str[4:5]

    return demand


def get_USPdemand():

    col = ['SAP Number', 2015, 2016, 2017, 2018, 2019, 'Total', 'Recommendation']
    col_rename = {'SAP Number':'Catalog_item'}

    demand_all = pd.read_excel(path, sheet_name="Summary USP", skiprows=2)
    demand_all.dropna(how="all")
    demand_notnull = demand_all[col]
    demand_notnull = demand_notnull[pd.notnull(demand_notnull.iloc[:,0])]

    # replace the 'SS' notation for the ASME 'AS' notation
    demand_notnull['SAP Number'] = demand_notnull['SAP Number'].str.replace("SS", "AS", case=False)

    # rename columns
    demand_notnull = demand_notnull.rename(col_rename, axis=1)

    # group by SAP Number
    demand_group = demand_notnull.groupby('Catalog_item').agg({2015:['sum'], 2016:['sum'], 2017:['sum'], 2018:['sum'],
                                                               2019:['sum'], 'Total':['sum']})
    demand_group['Catalog_Item'] = demand_group.index

    # reset index
    demand = demand_group.reset_index(drop=True)

    # add average demand per year
    years = len(demand.columns) - 1
    demand['avg_demand'] = demand['Total'] / years
    demand['100_percent'] = round(demand.avg_demand)
    demand['80_percent'] = round(demand.avg_demand * 0.8)
    demand['60_percent'] = round(demand.avg_demand * 0.6)
    demand['40_percent'] = round(demand.avg_demand * 0.4)
    demand['20_percent'] = round(demand.avg_demand * 0.2)
    demand['vessel_size'] = demand.Catalog_Item.str[5:7]
    demand['vessel_qty'] = demand.Catalog_Item.str[4:5]

    return demand


def get_LIdemand():
    col = ['Nalco Part Number', 2015, 2016, 2017, 2018, 'Total']
    col_rename = {'Nalco Part Number': 'Catalog_item'}

    demand_all = pd.read_excel(path, sheet_name="Summary LI", skiprows=2)
    demand_all.dropna(how="all")
    demand_notnull = demand_all[col]
    demand_notnull = demand_notnull[pd.notnull(demand_notnull.iloc[:, 0])]

    # rename columns
    demand_notnull = demand_notnull.rename(col_rename, axis=1)

    # group by SAP Number
    demand_group = demand_notnull.groupby('Catalog_item').agg(
        {2015: ['sum'], 2016: ['sum'], 2017: ['sum'], 2018: ['sum'], 'Total': ['sum']})
    demand_group['Catalog_Item'] = demand_group.index

    # reset index
    demand = demand_group.reset_index(drop=True)

    # add average demand per year
    years = len(demand.columns) - 1
    demand['avg_demand'] = demand['Total'] / years
    demand['100_percent'] = round(demand.avg_demand)
    demand['80_percent'] = round(demand.avg_demand * 0.8)
    demand['60_percent'] = round(demand.avg_demand * 0.6)
    demand['40_percent'] = round(demand.avg_demand * 0.4)
    demand['20_percent'] = round(demand.avg_demand * 0.2)
    demand['vessel_size'] = demand.Catalog_Item.str[5:7]
    demand['vessel_qty'] = demand.Catalog_Item.str[4:5]

    return demand


def get_HIdemand():
    col = ['Nalco Part Number', 2015, 2016, 2017, 2018, 'Total']
    col_rename = {'Nalco Part Number': 'Catalog_item'}

    demand_all = pd.read_excel(path, sheet_name="Summary HI", skiprows=2)
    demand_all.dropna(how="all")
    demand_notnull = demand_all[col]
    demand_notnull = demand_notnull[pd.notnull(demand_notnull.iloc[:, 0])]

    # rename columns
    demand_notnull = demand_notnull.rename(col_rename, axis=1)

    # group by SAP Number
    demand_group = demand_notnull.groupby('Catalog_item').agg(
        {2015: ['sum'], 2016: ['sum'], 2017: ['sum'], 2018: ['sum'], 'Total': ['sum']})
    demand_group['Catalog_Item'] = demand_group.index

    # reset index
    demand = demand_group.reset_index(drop=True)

    # add average demand per year
    years = len(demand.columns) - 1
    demand['avg_demand'] = demand['Total'] / years
    demand['100_percent'] = round(demand.avg_demand)
    demand['80_percent'] = round(demand.avg_demand * 0.8)
    demand['60_percent'] = round(demand.avg_demand * 0.6)
    demand['40_percent'] = round(demand.avg_demand * 0.4)
    demand['20_percent'] = round(demand.avg_demand * 0.2)
    demand['vessel_size'] = demand.Catalog_Item.str[5:7]
    demand['vessel_qty'] = demand.Catalog_Item.str[4:5]

    return demand

def get_demand(product_line):
    if 'USP' in product_line.upper():
        demand = get_USPdemand()

    elif 'LI' in product_line.upper():
        demand = get_LIdemand()
        if len(product_line) > 2:
            # filter demand to the specific line
            pass
    elif 'HI' in product_line.upper():
        demand = get_HIdemand()

    return demand

def get_demand_for_list(CatItems, product_line):
    """return the total demand for a subset of the product line
        give list of catalog items and the product line"""

    demand_all = get_demand(product_line)
    demand = demand_all[demand_all['Catalog_Item'].isin(CatItems)]

    return demand

# print(get_USPdemand())