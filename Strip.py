import numpy as np


def strip_obj(col):
    if col.dtypes == object:
        return (col.astype(str)
                   .str.strip()
                   .replace({'nan': np.nan}))
    return col