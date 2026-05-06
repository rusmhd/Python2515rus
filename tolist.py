#Rushil Mohamed 12508033
import pandas as pd, numpy as np
df=pd.read_csv("/content/Redingtonbal.csv")
df.drop_duplicates(inplace=True)
df.columns =(df.columns.str.strip().str.lower().str.replace(r'[^a-z0-9]+','_',regex=True))
df.reset_index(drop=True,inplace=True)
print(df.columns.tolist)