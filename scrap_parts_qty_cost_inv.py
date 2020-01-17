from Parts_Demand import *
from datetime import datetime
import os

# Set up the analysis
product_line = 'USP'
mfg_time = 10  # work days
yearly_sale = 0 # units sold per year on average

LeadTimeUSP = [4, 4.5, 5, 6, 8]
LeadTimeLI = [4, 5, 6, 8, 10]

###
# Quick switch between lead times
lead_times = LeadTimeUSP

inv_df, demand_df = inventory_to_consider(product_line, lead_times, yearly_sale, mfg_time)

print(inv_df.sample(25))



desc_obj = bom[bom.PartNumber == part].PartDesc
                desc = desc_obj.item()
                inv_df.loc[(catitem, lead, part), :] = (desc, lead_time, qty, price, cost)