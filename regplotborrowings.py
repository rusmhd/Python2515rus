#Rushil Mohamed 12508033
#Q2:  Use Seaborn's regplot to visualise the relationship between Borrowings (IV) and TotalAssets (DV)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
PATH = r'/content/Redingtonbal.csv'
df   = pd.read_csv(PATH, parse_dates=['Year'])
sns.regplot(x='Borrowings', y='TotalAssets',data=df, color='teal')
plt.title('Borrowings vs Total Assets')
plt.xlabel('Borrowings (₹ Cr)')
plt.ylabel('Total Assets (₹ Cr)')
plt.show()
