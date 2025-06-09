import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/Sample-Superstore.csv", encoding='latin-1')
df.head()
print(df.info())
print(df.describe())
print(df.columns)

df.drop_duplicates(inplace=True)
print("Shape after removing duplicates:", df.shape)

region_data = df.groupby('Region')[['Sales', 'Profit']].sum().sort_values(by='Profit', ascending=False)
print(region_data)
print("Category count:\n", df['Category'].value_counts())
print("Sub-Category count:\n", df['Sub-Category'].value_counts())


losses = df[df['Profit'] < 0]
print("Top losses:\n", losses[['State', 'Sales', 'Profit']].sort_values(by='Profit').head(10))

print(df[['Sales', 'Discount', 'Profit']].corr())


# Visualization: Top 10 Loss-Making States

top_losses = losses.sort_values(by='Profit').head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_losses['State'], top_losses['Profit'], color='red')
plt.xlabel('Profit')
plt.ylabel('State')
plt.title('Top 10 Loss-Making States')
plt.tight_layout()
plt.show()
# Key Observations


# 1. Texas, Colorado, and Illinois are the top loss-making states.
# 2. Discounts are negatively correlated with profit (-0.22), meaning higher discounts often reduce profit.
# 3. West and South regions are performing well in terms of profit.
# 4. Sub-categories like 'Chairs' and 'Tables' show frequent losses.