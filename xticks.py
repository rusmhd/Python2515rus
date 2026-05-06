#Q1 plot TotalAssets over Year as a line graph with title, axis labels, and grid.
#Rushil Mohamed 12508033
import pandas as pd
import matplotlib.pyplot as plt
df   = pd.read_csv(r'/content/Redingtonbal.csv', parse_dates=['Year'])
df.sort_values('Year', inplace=True)
plt.plot(df['Year'], df['TotalAssets'],
         marker='o', color='teal')
plt.title('Tata Steel – Total Assets')
plt.xlabel('Year')
plt.ylabel('Total Assets (₹ Cr)')
plt.xticks(rotation=45)
plt.show()
