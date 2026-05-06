#Rushil Mohamed 12508033

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("/content/Redingtonbal.csv")
avg=df["TotalAssets"].mean()
print((df["TotalAssets"]>avg).sum())
sns.scatterplot(data=df,x="TotalAssets",y="TotalLiabilities")
plt.show()