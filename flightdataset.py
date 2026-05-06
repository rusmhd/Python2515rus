#Rushil Mohamed
#Load the flights dataset and perform the following:Display the first 5 rows Display the last 5 rows Display the shape of the dataset
import seaborn as sns
df = sns.load_dataset('flights')
print(df.head())
print(df.tail())
print("Shape:", df.shape)