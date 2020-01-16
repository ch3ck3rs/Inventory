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

# print(inv_df)

if __name__ == "__main__":

    now = datetime.now()
    stamp = now.strftime("%m-%d-%y_%H-%M")

    title = "This is a list of parts and their associated cost that will need to be inventoried per vessel we keep in inventory"
    preper = "Lauren Coffman"
    notes = ""
    sum_dict = {"Tile": title, "Creation_Date": stamp, "Prepared_by":preper, "Notes":""}
    summary = pd.DataFrame.from_dict(sum_dict, orient='index')

    path = r"C:\Users\coffmlv\Documents\1_ESD\Inventory Lead Time\Results"
    base_name = "Results_Inventoried_Parts_"+stamp+".xlsx"
    writer = pd.ExcelWriter(os.path.join(path, base_name))

    summary.to_excel(writer, sheet_name='Summary')
    inv_df.to_excel(writer, sheet_name='Inventory')
    demand_df.to_excel(writer, sheet_name='Demand')

    writer.save()
