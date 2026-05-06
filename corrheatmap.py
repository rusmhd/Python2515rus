#Q7:  Create a correlation heatmap for FixedAssets, Investments, Borrowings, Reserves, and TotalAssets.
#Rushil Mohamed 12508033
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
PATH = r'/content/Redingtonbal.csv'
df   = pd.read_csv(PATH, parse_dates=['Year'])

cols = ['FixedAssets','Investments',
        'Borrowings','Reserves',
        'TotalAssets']
sns.heatmap(df[cols].corr(), annot=True,
            cmap='coolwarm', fmt='.2f')
plt.title('Tata Steel – Correlation Heatmap')
plt.show()