import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("algorithmic-trading-dataset.csv")

# Top 10 momentum stocks based on Momentum Score
df['Momentum Score'] = df['Momentum Score'].str.replace('%', '').astype(float)
top_10_momentum = df.nlargest(10, 'Momentum Score')[['Ticker', 'Momentum Score']]
print("\nTop 10 Momentum Stocks:\n", top_10_momentum)

# Ploting bar chart
plt.figure(figsize=(10, 6))
sns.barplot(data=top_10_momentum, x='Ticker', y='Momentum Score', hue='Ticker', 
            palette='viridis', legend=False)
plt.title('Top 10 Momentum Stocks')
plt.xlabel('Ticker')
plt.ylabel('Momentum Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_10_momentum_barplot.png')
plt.show()