#Rushil Mohamed 12508033
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("TotalLiabilities").corr(df["TotalAssets"])
sns.regplot(data=df,x="TotalLiabilities",y="TotalAssets")
plt.show()