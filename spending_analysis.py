import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

# Summary stats
print(df.describe())

# Gender distribution
sns.countplot(data=df, x='Gender')
plt.title('Gender Distribution')
plt.savefig("gender_distribution.png")
plt.clf()

# Age distribution
sns.histplot(data=df, x='Age', bins=15, kde=True)
plt.title('Age Distribution')
plt.savefig("age_distribution.png")
plt.clf()

# Income vs Spending Score
sns.scatterplot(data=df, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Gender')
plt.title('Income vs Spending Score')
plt.savefig("income_vs_spending.png")
plt.clf()

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.clf()
