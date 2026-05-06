#Rushil Mohamed
#Using the flights dataset: Display records where year = 1955Display records where month = 'January' Display records where passengers > 400
import seaborn as sns
df = sns.load_dataset('flights')
print(df[df['year'] == 1955])
print(df[df['month'] == 'January'])
print(df[df['passengers'] > 400])