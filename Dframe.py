#Rushil Mohamed 12508033
import pandas as pd, numpy as np
df=pd.read_csv("/content/Redingtonbal.csv")

high=df[df['TotalAssets']>200000]
print(high[['Year','TotalAssets']])

both=df[(df["TotalAssets"] > 200000) & (df['TAD'] == 1)]
print(both[['Year',"TotalAssets",'TAD']])