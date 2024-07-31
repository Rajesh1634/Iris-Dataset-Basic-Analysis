import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv" 
iris = pd.read_csv(url)

# Display the first few rows of the dataset
print(iris.head())

# Display summary statistics
print(iris.describe())

# Pairplot
sns.pairplot(iris, hue='species')
plt.show()
 
# Boxplot
sns.boxplot(x='species', y='sepal_length', data=iris)
plt.show()

# # Correlation Heatmap

corr = iris.drop(columns='species').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

# Export Data to CSV (if needed for Power BI or Tableau)
iris.to_csv('iris_dataset.csv', index=False)
