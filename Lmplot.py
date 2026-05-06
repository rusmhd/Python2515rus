#Q9:  Use lmplot to show Borrowings (IV) vs TotalLiabilities (DV) with separate regression lines by TAD group.
#Rushil Mohamed 12508033
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
PATH = r'/content/Redingtonbal.csv'
df   = pd.read_csv(PATH, parse_dates=['Year'])
df['TAD'] = df['TAD'].astype(str)

sns.lmplot(x='Borrowings',
           y='TotalLiabilities',
           data=df, hue='TAD',
           palette='Set1')
plt.title('Borrowings vs Liabilities by TAD')
plt.show()
