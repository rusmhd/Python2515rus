#Rushil Mohamed 12508033
import pandas as pd , numpy as np
df=pd.read_csv("/content/Redingtonbal.csv")
df['debt_to_equity'] = df["Borrowings"]  / df['EquityCapital']
df["asset_util"] = df["TotalLiabilities"] / df["TotalAssets"]
df["invest_ratio"] = df["Investments"] / df["TotalAssets"]
print(df[['debt_to_equity',"asset_util","invest_ratio"]].round(3))