from PTSDemand import *
from Parts_Inventory import *
from Parts_Final import *


def inventory_to_consider(product_line, lead_times, yearly_sale=None, mfg_time=None):
    """This returns the price per unit to be inventoried at given leadtime.  output in a MultiIndex DataFrame
            Index = [CatalogItem, LeadTime, Part]
            Columns = [Lead, Cost : (price * qty)]"""

    yearly_sale = yearly_sale or 1  # minimum number of units sold per year at the line item level
    # mfg_time has a default value set within get_partslist()

    ###
    # Pull in needed data
    demand = get_demand(product_line)

    catitems = get_products(product_line)

    df_cost, df_list = get_partslist(catitems, lead_times, mfg_time)

    ###
    # filter catalog to only those products with yearly demand >= yearly_sale
    consider_demand = demand[round(demand['avg_demand']) >= yearly_sale]

    consider_catalog = consider_demand['Catalog_Item'].tolist()

    ###
    # loop through catalog items to consider and append parts that are on the Inventory list
    inv_df = pd.DataFrame(columns=['CatalogItem', 'TopLevel_LeadTime', 'Part', 'Item_LeadTime', 'Cost_per_unit'])
    inv_df = inv_df.set_index(['CatalogItem', 'TopLevel_LeadTime', 'Part'])
    inv_df = inv_df.astype('float64')

    for row in df_list.iterrows():
        catitem = row[0][0]
        if catitem in consider_catalog:
            lead = row[0][1]
            parts_list = getattr(row[1], 'Inv_Parts')
            bom = get_bom(catitem)
            # print(catitem, '\n', parts_list, '\n', lead, '\n', '------------------', '\n')
            for part in parts_list:
                lead_time = leadtime.lead[leadtime.lead.Material == part].PlannedLeadTime.item()
                price = leadtime.lead[leadtime.lead.Material == part].NetPrice.item()
                qty_ = bom[bom.PartNumber == part].BomQty.max()
                qty = qty_.item()
                cost = price * qty
                inv_df.loc[(catitem, lead, part), :] = (lead_time, cost)

    return inv_df, demand


def cost_per_dmnd(product_line, lead_times, yearly_sale=None, mfg_time=None):

    per_unit, demand = inventory_to_consider(product_line, lead_times, yearly_sale, mfg_time)
    per_unit_sum = per_unit['Cost_per_unit'].groupby(level=[1, 0]).sum().round(2).to_frame()

    per_dmnd_cost = pd.DataFrame(columns=['TopLevel_LeadTime', 'CatalogItem', 'per_1.0_dmnd', 'per_0.8_dmnd', 'per_0.6_dmnd',
                                          'per_0.4_dmnd', 'per_0.2_dmnd']).set_index(['TopLevel_LeadTime', 'CatalogItem'])

    for idx, row in per_unit_sum.iterrows():
        catitem = row.name[1]
        dmd = demand[demand['Catalog_Item'] == catitem]['avg_demand'].item()
        cpu = row['Cost_per_unit']
        risk = [1.0, 0.8, 0.6, 0.4, 0.2]
        cost = []
        for percent in risk:
            cost.append(round(percent * dmd) * cpu)
        data = pd.Series(cost, index=['per_1.0_dmnd', 'per_0.8_dmnd', 'per_0.6_dmnd', 'per_0.4_dmnd', 'per_0.2_dmnd'])
        data.name = idx
        per_dmnd_cost = per_dmnd_cost.append(data)

    return demand, per_unit, per_dmnd_cost


###
# Set up the analysis
product_line = 'USP'
mfg_time = 10  # work days
yearly_sale = 1 # units sold per year on average

LeadTimeUSP = [3, 3.5, 4, 5]
LeadTimeLI = [4, 5, 6, 8, 10]

###
# Quick switch between lead times
lead_times = LeadTimeUSP

###
# Analysis test

# df = inventory_to_consider(product_line, LeadTimes, yearly_sale, mfg_time)

# demand = get_demand(product_line)

df = cost_per_dmnd(product_line, lead_times, yearly_sale, mfg_time)



