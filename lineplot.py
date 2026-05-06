#Rushil Mohamed 12508033
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("/content/Redingtonbal.csv")
print(df["TotalLiabilities"].median())
sns.lineplot(data=df,x="Year",y="TotalLiabilities")