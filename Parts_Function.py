import CatalogTracker as tracker


def in_standard(product_line, item_list):
    """takes product line and list of catalog items, returns list of tuples in the form
            [ (item, T/F in catalog) , (item, T/F), ... ] """

    catalog_df = tracker.catalog.loc[tracker.catalog['Product Line'].str.contains(product_line, na=False)]
    catalog = catalog_df['SAP Product Number'].tolist()
    standard = []

    for item in item_list:

        inCat = item in catalog
        result = (item, inCat)
        standard.append(result)

    return standard