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
    demand = demand.groupby('Catalog_item').agg({2010:['sum'], 2011:['sum'], 2012:['sum'], 2013:['sum'], 2014:['sum'],
                                                 2015:['sum'], 2016:['sum'], 2017:['sum'], 2018:['sum'], 'Total':['sum']})

    return demand


def get_USPdemand():

    col = ['SAP Number', 2015, 2016, 2017, 2018, 'Total', 'Recommendation']
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
    demand = demand_notnull.groupby('Catalog_item').agg({2015:['sum'], 2016:['sum'], 2017:['sum'], 2018:['sum'], 'Total':['sum']})

    return demand


def get_LIDemand():
    col = ['Nalco Part Number', 2015, 2016, 2017, 2018, 'Total']
    col_rename = {'Nalco Part Number': 'Catalog_item'}

    demand_all = pd.read_excel(path, sheet_name="Summary LI", skiprows=2)
    demand_all.dropna(how="all")
    demand_notnull = demand_all[col]
    demand_notnull = demand_notnull[pd.notnull(demand_notnull.iloc[:, 0])]

    # rename columns
    demand_notnull = demand_notnull.rename(col_rename, axis=1)

    # group by SAP Number
    demand = demand_notnull.groupby('Catalog_item').agg(
        {2015: ['sum'], 2016: ['sum'], 2017: ['sum'], 2018: ['sum'], 'Total': ['sum']})

    return demand


def get_HIDemand():
    col = ['Nalco Part Number', 2015, 2016, 2017, 2018, 'Total']
    col_rename = {'Nalco Part Number': 'Catalog_item'}

    demand_all = pd.read_excel(path, sheet_name="Summary HI", skiprows=2)
    demand_all.dropna(how="all")
    demand_notnull = demand_all[col]
    demand_notnull = demand_notnull[pd.notnull(demand_notnull.iloc[:, 0])]

    # rename columns
    demand_notnull = demand_notnull.rename(col_rename, axis=1)

    # group by SAP Number
    demand = demand_notnull.groupby('Catalog_item').agg(
        {2015: ['sum'], 2016: ['sum'], 2017: ['sum'], 2018: ['sum'], 'Total': ['sum']})

    return demand


# print(get_LIDemand().head())