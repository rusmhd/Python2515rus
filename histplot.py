#Q3:  Plot the distribution of Reserves using histplot with a KDE curve overlaid.
#Rushil Mohamed 12508033
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
PATH = r'/content/Redingtonbal.csv'
df   = pd.read_csv(PATH, parse_dates=['Year'])

sns.histplot(df['Reserves'], kde=True,
             color='steelblue', bins=8)
plt.title('Distribution of Reserves')
plt.xlabel('Reserves (₹ Cr)')
plt.ylabel('Frequency')
plt.show()