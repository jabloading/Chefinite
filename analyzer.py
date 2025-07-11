import json
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load sample data
with open("data/sample_data.json") as f:
    restaurants = json.load(f)

# Collect all dishes from every restaurant
all_dishes = []
for r in restaurants:
    all_dishes.extend(r["top_dishes"])

# Count frequency of each dish
dish_counts = Counter(all_dishes)

# Save to CSV
os.makedirs("output", exist_ok=True)
df = pd.DataFrame(dish_counts.items(), columns=["Dish", "Count"])
df = df.sort_values(by="Count", ascending=False)
df.to_csv("output/top_dishes.csv", index=False)

# Plot bar chart
plt.figure(figsize=(10, 6))
plt.bar(df["Dish"], df["Count"], color="tomato")
plt.xticks(rotation=45, ha="right")
plt.title("🍽️ Most Popular Dishes (Sample ZIP: 90001)")
plt.tight_layout()
plt.savefig("output/chart.png")

print("✅ Analysis complete: 'top_dishes.csv' and 'chart.png' saved to output/")
