#Rushil Mohamed 12508033
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("/content/Redingtonbal.csv")

avg=df["Borrowings"].mean()
df=df[df["Borrowings"]> avg]
print(df["Borrowings"].mean())
sns.scatterplot(data=df,x="Borrowings",y="TotalAssets")
plt.show()