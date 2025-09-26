import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter
import random

def simulate_rolls(n=1000):
    results = [random.randint(1,6) + random.randint(1,6) for _ in range(n)]
    return results

def plot_results(results):
    frequencies = Counter(results)
    plt.bar(frequencies.keys(), frequencies.values())
    plt.xlabel("Sum of the dice")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of sums ({len(results)} rolls)")
    plt.savefig("../dice_distribution.png")
    plt.close()

if __name__ == "__main__":
    rolls = simulate_rolls()
    plot_results(rolls)
    print("Plot saved as dice_distribution.png")
