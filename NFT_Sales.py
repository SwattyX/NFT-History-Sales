# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 21:24:02 2021

@author: JOSEP
"""

import pandas as pd
import numpy as np
import matplotlib

df = pd.read_csv("NFT_Sales.csv")
nft_df = df
nft_df.head()
nft_df["NaN"] = df.apply(lambda x: 1 if x.isna() else 0, axis=1)
missing_values = nft_df.isnull()
nft_df["NaN"] = missing_values.apply(lambda x: 1 if x else 0, axis=1)

for col in missing_values.columns:
    print(col)
    print(nft_df[col].isnull().any())
    nft_df["NaN"] = nft_df[col].isnull().any()
    # nft_df=groupby(by="Year").count()

nft_df["NaN"] = missing_values["Date"].apply(lambda x: 1 if x else x)
nft_df["col1"].isnull().any()
