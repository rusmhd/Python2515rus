#Rushil Mohamed 12508033
import pandas as pd ,numpy as np
df=pd.read_csv("/content/Redingtonbal.csv")
num=df.select_dtypes(include=[np.number]).columns
stats=pd.DataFrame({'Mean':df[num].mean(),'Median':df[num].median(),'Min':df[num].min(),'Max':df[num].max(),"Std":df[num].std()})
print(stats.round(2))
