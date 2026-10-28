
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books_data.csv")

df["Price_Number"] = (
    df["Price"]
    .astype(str)
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .str.strip()
    .astype(float)
)

data = df.head(10)

plt.figure(figsize=(13, 7))
bars = plt.bar(range(len(data)), data["Price_Number"])

labels = [
    title if len(title) <= 25 else title[:22] + "..."
    for title in data["Title"]
]

plt.xticks(range(len(labels)), labels, rotation=35, ha="right")
plt.bar_label(bars, fmt="£%.2f", padding=3)
plt.title("Book Price Analysis", fontsize=18, fontweight="bold")
plt.xlabel("Book Titles")
plt.ylabel("Price (£)")
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()

plt.savefig("books_price_graph.png", dpi=300, bbox_inches="tight")
plt.close()

print("SUCCESS! Graph saved as books_price_graph.png")
