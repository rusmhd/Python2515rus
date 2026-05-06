#Rushil Mohamed 12508033
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("/content/Redingtonbal.csv")
avg=df["Reserves"].mean()
c=0
for v in df["Reserves"]:
  if v > avg:
    c+=1
print(c)
sns.boxplot(data=df,y="Reserves")
plt.show()