#Rushil Mohamed 12508033
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("/content/Redingtonbal.csv")
print(df["TotalLiabilities"].corr(df["TotalAssets"]))
sns.regplot(data=df,x="TotalLiabilities",y="TotalAssets")
plt.show()
