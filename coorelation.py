#Q10:  Compute correlation between Borrowings and TotalAssets and print a prescriptive financial recommendation.
#Rushil Mohamed 12508033
import pandas as pd
import numpy as np
PATH = r'/content/Redingtonbal.csv'
df   = pd.read_csv(PATH, parse_dates=['Year'])

x = df['Borrowings'].values
y = df['TotalAssets'].values
r = np.corrcoef(x, y)[0, 1]

if r > 0.7:
    print('Debt-driven growth – REVIEW leverage')
elif r > 0.4:
    print('Moderate link – MONITOR borrowings')
else:
    print('Healthy – assets not debt-dependent')
print(f'Correlation = {r:.3f}')