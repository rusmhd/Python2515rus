#Rushil Mohamed 12508033
import pandas as pd
import numpy as np
df=pd.read_csv("/content/Redingtonbal.csv")
num_cols=['EquityCapital','Reserves','TotalAssets']
for col in num_cols:
  df[col]=pd.to_numeric(df[col],errors='coerce')
  print(df.dtypes)