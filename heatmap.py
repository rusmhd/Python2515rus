#Rushil Mohamed 12508033
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("/content/Redingtonbal.csv")
c=df.corr(numeric_only=True)
print(c)
sns.heatmap(c,annot=True)
plt.show()
