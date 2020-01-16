### Currently working on:  Demand Analysis

_Determine average demand per year and avg qty ordered_

bug in tracker. see bug log / issue 2

#### Demand_scrap.py
* consider means more than X orders per year on average at the catalog item level.  
    manually set in the function
* have a df of all boms to consider
* what do I need to consider?
    * Inventory_to_consider yields the price of inventory per unit needed
    * need to multiply by the forecast



TODO / ToThink
* get_LeadPart returns part for each cat_item in that product_line


Result_Inventory_USP.py
* initially set up to do the inventory analysis on basis of average.  
    * used Total Demand and % of BOMs to determine how many parts to inventory
    * analysis complete in inv_sum
        * cost_max    32,847,300
        * cost_avg    14,091,800
    * **This does not line up with gut check**
    