# File Structure

#### Changes made to file names that may not have changed in Jupyter
* switched '??_Parts.py' to 'Parts _ ??.py'
* Parts_Demand.py -> changed 'LeadTime' to 'TopLevel_LeadTime'
Parts_Demand.py -> changed 'Lead' to 'Item_Lead'

### Source files to change
* CatalogTracker.py     < Catalog/PTS Equip Standarsization Tracker.xlsx
* DataFrameBOMs.py      < Inventory Lead Time/BOMs/
* CostedMaterials.py    < Costing/ZCOST_ACC.xlsx
* P90LeadTimes.py       < Inventory Lead Time/Plant 90 Leadtimes - 10.24.19.csv
* P90MFGTimes.py        < Catalog/P90MFGTimes.csv
* PTSDemand.py          < Inventory Lead Time/GlenwoodProduction_clean.xlsx

### Structure
* Parts_???.py - are function files
* Results_____.py - output files to excel
*  % Analysis %.py are end result files

### Thoughts
* use get_final(), get_partslist(), and get_demand() as base data for the analysis
    * get_final() yields 3 DataFrames:
        * final[0] - returns the parts that appear in every bom for the product line
        * final[1] - returns the parts that appear in at least X% of boms, specified or default of 75%
        * final[2] - returns all parts that appear in the product line
    * get_partslist() yields 2 data frames
        * parts[0] or df_cost - returns the estimated cost of the parts that need to be inventoried at 
            given lead times specified in weeks
        * parts[1] or df_list - returns the part numbers that need to be inventoried at 
            the given lead times, specified in weeks
    * get_demand() - yields a DataFrame containing historical demand for a given product line

### Jupyter
There is a jupyter file Inventory Analysis 1.0.ipynb that starts to outline the data and looks at some graphs.

### Current bug log