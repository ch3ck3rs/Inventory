from PTSDemand import *
from Parts_Final import *

product_line = 'USP'
LeadTimes = [3, 3.5, 4, 5, 6]

# Below here will set up and inventory estimate based on total demand and average number of parts required per build
# TODO this does not return the expected results
###
# risk ratings => inventory_ratio is the % of avg years sales we should keep in inventory
# i.e. - if we sell 10 units per year, a ration of .2 means we should inventory enough for 2 units
inventory_ratio = .2

###
# call functions and gather data for the line and lead times above
catitems = get_products(product_line)

demand_total = get_demand(product_line)

df_cost, df_list = get_partslist(catitems, LeadTimes)

final, num, percent_for_most = get_final(product_line)

###
# set up the get_final data above
df_all = final[0]
df_most = final[1]
df_everything = final[2]

df_all_parts = df_all['Part'].tolist()
df_most_parts = df_most['Part'].tolist()

###
# set up for analysis
inventory = pd.DataFrame()
inv_list = []

###
# for parts that appear in ALL BOMs
#   taking the demand for all catalog items to determine the parts that should be inventoried
#   units_to_inventory is the total number of units that we should be able to make

if len(df_all) != 0:
    total_demand_yearly = int(sum(demand_total['avg_demand'].tolist()))
    units_to_inventory = int(total_demand_yearly * inventory_ratio)

    for index, row in df_all.iterrows():
        percent = row['Percent_of_BOMs']
        row['inv_max'] = int(row['qty_max'] * percent * units_to_inventory)
        row['inv_min'] = int(row['qty_min'] * percent * units_to_inventory)
        row['inv_avg'] = int(row['qty_avg'] * percent * units_to_inventory)
        inv_list.append(row)

    inventory = inventory.append(inv_list)


if len(df_most) != 0:
    total_demand_yearly = int(sum(demand_total['avg_demand'].tolist()))
    units_to_inventory = int(total_demand_yearly * inventory_ratio)

    for index, row in df_most.iterrows():

        if row['Part'] in df_all_parts:
            pass
        else:
            percent = row['Percent_of_BOMs']
            row['inv_max'] = int(row['qty_max'] * percent * units_to_inventory)
            row['inv_min'] = int(row['qty_min'] * percent * units_to_inventory)
            row['inv_avg'] = int(row['qty_avg'] * percent * units_to_inventory)
            inv_list.append(row)

        inventory = inventory.append(inv_list)

if len(df_everything) != 0:
    total_demand_yearly = int(sum(demand_total['avg_demand'].tolist()))
    units_to_inventory = int(total_demand_yearly * inventory_ratio)

    for index, row in df_everything.iterrows():

        if row['Part'] in df_most_parts:
            pass
        else:
            percent = row['Percent_of_BOMs']
            row['inv_max'] = int(row['qty_max'] * percent * units_to_inventory)
            row['inv_min'] = int(row['qty_min'] * percent * units_to_inventory)
            row['inv_avg'] = int(row['qty_avg'] * percent * units_to_inventory)
            inv_list.append(row)

        inventory = inventory.append(inv_list)

###
# summarize the Inventory df to show part, desc, inv_max, inv_avg, cost_max, cost_avg
# also output df.sum to get total costs


def cost(price, qty):
    # return the cost to inventory parts
    return price * qty


inv_col = ['Part', 'description', 'price', 'inv_max', 'inv_avg']

inv_sum = inventory[inv_col].copy()
inv_sum['cost_max'] = cost(inv_sum['price'], inv_sum['inv_max'])
inv_sum['cost_avg'] = cost(inv_sum['price'], inv_sum['inv_avg'])

# print(inv_sum.sum())
