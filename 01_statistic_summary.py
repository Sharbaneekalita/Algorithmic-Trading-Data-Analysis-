import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("algorithmic-trading-dataset.csv")

# Clean the Price column (remove '$' and convert to float)
df["Price"] = df["Price"].replace(r'[\$,]', '', regex=True).astype(float)

# Convert return columns to float
return_columns = [
    "One Year Price Return", "Six Month Price Return",
    "Three Month Price Return", "One Month Price Return"
]
for col in return_columns:
    df[col] = df[col].str.replace('%', '').astype(float)

# Statistics Summary (mean, median, std) of returns
summary_stats = df[return_columns].agg(['mean', 'median', 'std'])
summary_stats.index = summary_stats.index.str.capitalize()

# Ploting in table
fig, ax = plt.subplots(figsize=(8, 2))
ax.axis('off')

table = ax.table(
    cellText=summary_stats.values,
    rowLabels=summary_stats.index,
    colLabels=summary_stats.columns,
    loc='center',
    cellLoc='center',
    colLoc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.title("Summary Statistics of Returns", fontweight="bold", pad=20)
plt.tight_layout()
plt.savefig("summary_statistics_table.png")
plt.show()