#Q4:  Create boxplots for FixedAssets and Investments to compare distributions and identify outliers.
#Rushil Mohamed 12508033
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
PATH = r'/content/Redingtonbal.csv'
df   = pd.read_csv(PATH, parse_dates=['Year'])

cols = ['FixedAssets', 'Investments']
df_m = df[cols].melt(
    var_name='Type', value_name='Value')
sns.boxplot(x='Type', y='Value',
            data=df_m, palette='Set2')
plt.title('FixedAssets vs Investments')
plt.show()