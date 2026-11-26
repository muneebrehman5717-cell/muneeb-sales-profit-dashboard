# Business Sales Dashboard with Profit Margin
# Sales, Expenses, Profit (Bars) + Profit Margin % (Line)

import matplotlib.pyplot as plt
import numpy as np

shops = ["Shop A", "Shop B", "Shop C", "Shop D"]
sales    = [120000, 150000, 90000, 180000]
expenses = [85000, 100000, 75000, 160000]
profit   = [35000, 50000, 15000, 20000]

# Profit Margin = Profit / Sales * 100
profit_margin = []
for i in range(len(shops)):
    margin = (profit[i] / sales[i] * 100)
    profit_margin.append(margin)

x = np.arange(len(shops))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 6))

# Bars
ax.bar(x - width, sales,    width, color="#2563eb", label="Sales")
ax.bar(x,          expenses, width, color="#ef4444", label="Expenses")
ax.bar(x + width,  profit,   width, color="#22c55e", label="Profit")

ax.set_xticks(x)
ax.set_xticklabels(shops)
ax.set_title("Business Sales Performance", fontsize=16, fontweight="bold", pad=15)
ax.set_xlabel("Shops")
ax.set_ylabel("Rs (Amount)")
ax.grid(axis="y", linestyle="--", alpha=0.5)
ax.set_axisbelow(True)

# Profit Margin Line (Right Side)
ax2 = ax.twinx()
ax2.plot(x, profit_margin, color="#f97316", marker="o", linewidth=2.5, markersize=8, label="Profit Margin %")
ax2.set_ylabel("Profit Margin (%)")
ax2.set_ylim(0, 50)

# Margin % Likho Upar
for i, val in enumerate(profit_margin):
    ax2.text(x[i], val + 1.5, f"{val:.1f}%", ha="center", fontsize=10, fontweight="bold", color="#f97316")

# Dono Legend Ek Saath
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

plt.tight_layout()
plt.savefig("dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
