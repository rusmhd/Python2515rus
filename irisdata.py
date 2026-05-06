#Rushil Mohamed 12508033
#iris datset and display first 5 rows , disaply column anmes, shape of the datset
import seaborn as sns
df=sns.load_dataset("iris")
print(df.head())
print(df.columns.tolist())
print("shape",df.shape)