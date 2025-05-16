import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("algorithmic-trading-dataset.csv")

# Categorize stocks into momentum tiers
def categorize(score):
    if score >= 95:
        return "High"
    elif score >= 85:
        return "Medium"
    else:
        return "Low"

df["Momentum Tier"] = df["Momentum Score"].apply(categorize)
tier_counts = df["Momentum Tier"].value_counts()

explode = [0.05] * len(tier_counts)

# Ploting pie chart
plt.figure(figsize=(7, 7))
plt.pie(tier_counts, labels=tier_counts.index, autopct='%1.1f%%',
        startangle=140, colors=['green', 'orange', 'red'][:len(tier_counts)], explode=explode)
plt.title('Distribution of Momentum Tiers')
plt.tight_layout()
plt.show()