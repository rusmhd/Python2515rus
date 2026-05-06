#Rushil Mohamed 12508033
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("/content/Redingtonbal.csv")
vals=list(df["TotalAssets"])
print(sum(vals)/len(vals))
sns.violinplot(data=df,y="TotalAssets")
plt.show()