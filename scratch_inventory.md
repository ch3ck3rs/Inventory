### Currently working on:  **get_Final('LI')**
  * ~~make **get_products** more robust to accept LIKE~~
  * ~~improve **get_common**~~
  * get_Final line 48: all1 merge
    * getting key error on 'part' for LI but not for USP.
    * trace into get_Inventory
  * ~~merge key error with **get_Inventory**~~ << likely due to get_common.all returning an empty dataframe
    * ~~TODO getting key error on 'part' for LI but not for USP.~~
      * ~~due to improper inputs~~
    * ~~**get_leadPart(part, line)**~~ returns the same for USP and LI
      * ~~does leadPart return different for USP and LI?~~  **NO**
      * works with LI
      * calls
        * ~~get_CatalogItems(part)~~ returns the same
        * ~~tracker.catalog~~ returns the same
        * ~~leadtime.lead~~
    * trace into **get_common(product_list)**
        * **_`get_common can return and empty data frame`_**
        * change this to return an list of dataframes, not 3 seperate dfs



TODO / ToThink
* get_LeadPart returns part for each cat_item in that product_line



get_Final(product_line)
- works with USP
- not with LI, HI, RO
    * **_`get_common can return and empty data frame`_**

