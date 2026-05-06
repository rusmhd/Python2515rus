#Q6:  Plot a grouped bar chart comparing EquityCapital and Reserves for each year
#Rushil Mohamed 12508033
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
PATH = r'/content/Redingtonbal.csv'
df   = pd.read_csv(PATH, parse_dates=['Year'])
x = np.arange(len(df))
plt.bar(x - 0.2, df['EquityCapital'],
        width=0.4, label='Equity')
plt.bar(x + 0.2, df['Reserves'],
        width=0.4, label='Reserves')
plt.xticks(x, df['Year'].dt.year, rotation=45)
plt.title('Equity Capital vs Reserves')
plt.legend(); plt.tight_layout()
plt.show()