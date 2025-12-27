<!-- import numpy as np
import matplotlib.pyplot as plt

# Bitloops brand color
BITLOOPS_PURPLE = "#7404e4"

# X-axis: Task drift / long-tailness (0 = fully stable, 1 = highly drifting/long-tail)
x = np.linspace(0, 1, 400)

# Define "efficient" anchor points (best tool per regime)
# These represent dominant deployments only (used to fit frontier)
efficient_points = np.array([
    (0.05, 1.25),  # Algorithm for F->C
    (0.35, 0.90),  # Specialized ML for spam
    (0.55, 0.72),  # LLM for intent translation
    (0.85, 0.68),  # Human escalation handling
])

# Fit a smooth curve through efficient points
coef = np.polyfit(efficient_points[:, 0], efficient_points[:, 1], deg=3)
frontier_y = np.polyval(coef, x)

# All viable deployments (including dominated ones)
deployments = [
    # F -> C
    ("Algorithm for °F→°C", 0.05, 1.25),
    ("Human for °F→°C", 0.05, 0.55),
    ("LLM for °F→°C", 0.05, 0.30),
    ("ML for °F→°C", 0.05, 0.45),

    # Spam
    ("Specialized ML for Spam", 0.35, 0.90),
    ("LLM for Spam", 0.35, 0.45),
    ("Human for Spam", 0.35, 0.30),

    # Intent translation
    ("LLM for Intent Translation", 0.55, 0.72),
    ("Human for Intent Translation", 0.55, 0.55),

    # Escalation
    ("Human Escalation Handling", 0.85, 0.68),
    ("LLM-only Escalation Handling", 0.85, 0.25),
]

plt.figure(figsize=(11, 6.5))

# Plot frontier
plt.plot(
    x,
    frontier_y,
    linewidth=3,
    color=BITLOOPS_PURPLE,
    label="Efficiency frontier (best achievable)",
)

# Plot dominated region
plt.fill_between(
    x,
    0,
    frontier_y,
    color=BITLOOPS_PURPLE,
    alpha=0.12,
    label="Dominated deployments",
)

# Plot deployments
for name, xi, yi in deployments:
    plt.scatter(xi, yi, s=70, zorder=3, color="black")
    plt.annotate(
        name,
        (xi, yi),
        textcoords="offset points",
        xytext=(6, 6),
        ha="left",
        fontsize=9,
    )

plt.xlabel("Task drift & long-tailness (low → high)")
plt.ylabel("Effective outcomes per unit cost (higher is better)")
plt.title("Efficiency Frontier of Intelligence: Right Tool for the Right Work")
plt.grid(True, linestyle=":", linewidth=0.7)
plt.legend(loc="upper right", fontsize=9)

out_path = "/mnt/data/efficiency_frontier_bitloops.png"
plt.tight_layout()
plt.savefig(out_path, dpi=200)
plt.show() -->