import seaborn as sns
import matplotlib.pyplot as plt

# Load built-in dataset
df = sns.load_dataset('tips')
print(df.head())

# 1. Scatter Plot
sns.scatterplot(data=df, x='total_bill', y='tip')
plt.title("Total Bill vs Tip")
plt.show()

# 2. Line Plot
sns.lineplot(data=df, x='size', y='total_bill')
plt.title("Size vs Total Bill")
plt.show()

# 3. Bar Plot
sns.barplot(data=df, x='day', y='total_bill')
plt.title("Average Bill by Day")
plt.show()


# 4. Box Plot
sns.boxplot(data=df, x='day', y='total_bill')
plt.title("Total Bill Distribution by Day")
plt.show()


# 5. Histogram
sns.histplot(data=df, x='total_bill', bins=20, kde=True)
plt.title("Histogram of Total Bill")
plt.show()


# 6. Heatmap
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# 7. Pair Plot  
sns.pairplot(data=df, vars=['total_bill', 'tip', 'size'])
plt.title("Pair Plot of Total Bill, Tip, and Size")
plt.show()



