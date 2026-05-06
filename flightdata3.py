#Rushil Mohamed
#Using the flights dataset:Find the total passengers in 195 Find the average passengers for each year Find the maximum passengers in the dataset
import seaborn as sns
df = sns.load_dataset('flights')
mask  = df['year'] == 1950
total = df[mask]['passengers'].sum()
print("Total (1950):", total)
g   = df.groupby('year')
avg = g['passengers'].mean()
print("Avg per year:", avg)
print("Max:", df['passengers'].max())