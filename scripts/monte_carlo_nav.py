import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("outputs/nav_with_returns.csv")

returns = df["daily_return"].dropna()

mean = returns.mean()
std = returns.std()

days = 252 * 5
simulations = 100

results = np.zeros((days, simulations))

for i in range(simulations):
    price = 100

    for j in range(days):
        price *= (1 + np.random.normal(mean, std))
        results[j, i] = price

plt.figure(figsize=(10,6))

for i in range(simulations):
    plt.plot(results[:, i], alpha=0.1)

plt.title("Monte Carlo NAV Projection")
plt.xlabel("Trading Days")
plt.ylabel("Projected NAV")

plt.savefig("outputs/monte_carlo_projection.png")

plt.show()