import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Show summary statistics
print("Dataset Information:")
print(df.describe())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Count Movies vs TV Shows
plt.figure(figsize=(6,4))
sns.countplot(x="type", data=df)
plt.title("Movies vs TV Shows on Netflix")
plt.show()

# Top 10 countries
plt.figure(figsize=(10,5))
df["country"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Countries with Netflix Content")
plt.show()

# Release year trend
plt.figure(figsize=(10,5))
df["release_year"].value_counts().sort_index().plot(kind="line")
plt.title("Netflix Content Release Trend")
plt.show()

print("Task 3 Completed!")