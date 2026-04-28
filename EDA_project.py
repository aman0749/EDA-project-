import pandas as pd

df = pd.read_csv("eda_retail_dataset.csv")

print(df.head())


# Basic info
print(df.info())

# Statistical summary
print(df.describe())

# Check missing values
print(df.isnull().sum())

print(df['Store'].unique())
print(df['Product_Category'].unique())


category_rev = df.groupby('Product_Category')['Revenue'].sum()
print(category_rev)

store_rev = df.groupby('Store')['Revenue'].sum()
print(store_rev)


discount_rev = df.groupby('Discount_%')['Revenue'].mean()
print(discount_rev)

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

monthly_rev = df.groupby('Month')['Revenue'].sum()
print(monthly_rev)


#  step 4
import matplotlib.pyplot as plt

category_rev.plot(kind='bar')
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()

store_rev.plot(kind='bar')
plt.title("Revenue by Store")
plt.show()

monthly_rev.plot(kind='line')
plt.title("Monthly Revenue Trend")
plt.show()


import seaborn as sns
sns.heatmap(df.corr(), annot=True)
plt.show()

sns.boxplot(x='Product_Category', y='Revenue', data=df)
plt.show()