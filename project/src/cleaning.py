import pandas as pd
import numpy as np

def fill_missing_median(df, columns):
    out = df.copy()
    for col in columns:
        med = out[col].median()
        out[col] = out[col].fillna(med)
    return out

def drop_missing(df, how="any", threshold=None):
    out = df.copy()
    if threshold is not None:
        min_non_na = int(np.ceil(len(out.columns) * threshold))
        out = out.dropna(thresh=min_non_na)
    else:
        out = out.dropna(how=how)
    return out

def normalize_data(df, columns, method="zscore"):
    out = df.copy()
    for col in columns:
        x = pd.to_numeric(out[col], errors="coerce")
        if method == "zscore":
            mu, sigma = x.mean(), x.std(ddof=0)
            out[col] = 0.0 if (sigma == 0 or pd.isna(sigma)) else (x - mu) / sigma
        elif method == "minmax":
            lo, hi = x.min(), x.max()
            denom = hi - lo
            out[col] = 0.0 if (denom == 0 or pd.isna(denom)) else (x - lo) / denom
        else:
            raise ValueError("method must be 'zscore' or 'minmax'")
    return out
