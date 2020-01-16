import pandas as pd
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 150)

from PTSDemand import get_demand
from Parts_Demand import inventory_to_consider as consider


demand = get_demand('USP')

product_line = 'USP'
mfg_time = 10  # work days
yearly_sale = 0 # units sold per year on average
LeadTime = [3, 3.5, 4, 5, 10, 20]

per_unit = consider(product_line, LeadTime, yearly_sale, mfg_time)

per_unit_sum = per_unit['Cost_per_unit'].groupby(level=[1,0]).sum().round(2).to_frame()

per_dmnd_cost = pd.DataFrame(columns=['LeadTime', 'CatalogItem', 'per_1.0_dmnd', 'per_0.8_dmnd', 'per_0.6_dmnd',
                                      'per_0.4_dmnd', 'per_0.2_dmnd']).set_index(['LeadTime', 'CatalogItem'])

for idx, row in per_unit_sum.iterrows():
    catitem = row.name[1]
    dmd = demand[demand['Catalog_Item'] == catitem]['avg_demand'].item()
    cpu = row['Cost_per_unit']
    risk = [1.0, 0.8, 0.6, 0.4, 0.2]
    cost = []
    for percent in risk:
        cost.append(percent * dmd* cpu)
    data = pd.Series(cost, index=['per_1.0_dmnd', 'per_0.8_dmnd', 'per_0.6_dmnd', 'per_0.4_dmnd', 'per_0.2_dmnd'])
    data.name = idx
    per_dmnd_cost = per_dmnd_cost.append(data)


print(per_dmnd_cost)