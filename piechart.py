#Q8:  For the most recent year , plot a pie chart showing FixedAssets, CWIP, Investments, and OtherAssets.
#Rushil Mohamed 12508033
import pandas as pd
import matplotlib.pyplot as plt
PATH = r'/content/Redingtonbal.csv'
df   = pd.read_csv(PATH, parse_dates=['Year'])
latest = df.iloc[-1]
labels = ['FixedAssets','CWIP',
          'Investments','OtherAssets']
values = [latest[l] for l in labels]
plt.pie(values, labels=labels,
        autopct='%1.1f%%', startangle=140)
plt.title(f'Asset Mix – {latest["Year"].year}')
plt.show()