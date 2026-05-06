#Rushil Mohamed 12508033
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("/content/Redingtonbal.csv")
sns.regplot(data=df,x="Year",y="TotalLiabilities")
plt.show()