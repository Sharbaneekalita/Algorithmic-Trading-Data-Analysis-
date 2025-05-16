import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("algorithmic-trading-dataset.csv")

return_columns = [
    "One Year Price Return", "Six Month Price Return",
    "Three Month Price Return", "One Month Price Return"
]
for col in return_columns:
    df[col] = df[col].str.replace('%', '').astype(float)

df['Momentum Score'] = df['Momentum Score'].str.replace('%', '').astype(float)
top_10_momentum = df.nlargest(10, 'Momentum Score')[['Ticker', 'Momentum Score']]
top_5 = top_10_momentum['Ticker'].head(5).tolist()
top_5_df = df[df['Ticker'].isin(top_5)]

short_names = {
    "One Year Price Return": "1Y",
    "Six Month Price Return": "6M",
    "Three Month Price Return": "3M",
    "One Month Price Return": "1M"
}

# Line plot for price returns across different intervals (top 5 tickers)
melted = top_5_df.melt(id_vars='Ticker', value_vars=return_columns, 
                       var_name='Return Period', value_name='Return')
melted['Return Period'] = melted['Return Period'].map(short_names)
plt.figure(figsize=(10, 6))
sns.lineplot(data=melted, x='Return Period', y='Return', hue='Ticker', marker="o")
plt.title('Returns Over Time for Top 5 Momentum Stocks')
plt.xlabel('Return Period')
plt.ylabel('Return')
plt.tight_layout()
plt.savefig('top_5_returns_lineplot.png')
plt.show()