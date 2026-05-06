#using the iris dataset find tje averahe serpal lenght find the the maximum petal lenght find the minimum sepal width
import seaborn as snsw
df=sns.load_dataset("iris")
print("Avg sepal_length:",df['sepal_length'].mean())
print("Max petal_length:",df['petal_length'].max())
print("Min sepal_width:",df['sepal_width'].min())

