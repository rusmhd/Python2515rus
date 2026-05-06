#Rushil Mohamed 12508033
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("/content/Redingtonbal.csv")
avg=df["TotalLiabilities"].mean()
df=df[df["TotalLiabilities"]>avg]
print(df["TotalLiabilities"].mean())
sns.scatterplot(data=df,x="TotalLiabilities",y="TotalAssets")
plt.show()