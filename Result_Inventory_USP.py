from PTSDemand import *
from FinalParts import *

product_line = 'USP'
LeadTimes = [6, 8, 10, 12, 14]

###
# risk ratings => inventory_ratio is the % of avg years sales we should keep in inventory
# i.e. - if we sell 10 units per year, a ration of .2 means we should inventory enough for 2 units
inventory_ratio = .2

###
# call functions and gather data for the line and lead times above
catitems = get_products(product_line)

demand_total = get_demand(product_line)

df_cost, df_list = get_partslist(catitems, LeadTimes)

final, num, percent = get_final(product_line)

###
# set up the data above

df_all = final[0]
df_most = final[1]
df_everything = final[2]

###
# set up for analysis
inventory = {}

###
# for parts that appear in ALL BOMs

if len(df_all) != 0:
    total_demand_yearly = int(sum(demand_total['avg_demand'].tolist()))
    units_to_inventory = int(total_demand_yearly * inventory_ratio)



    print(units_to_inventory)
