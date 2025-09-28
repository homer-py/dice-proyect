import random
from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime
import os

# use the radint function to simulate rolls (random number 1-6 range)
def simulate_rolls(n=1000):
    return [random.randint(1,6) + random.randint(1,6) for _ in range(n)]

def plot_results(results):
    frequencies = Counter(results)
    plt.bar(frequencies.keys(), frequencies.values())
    plt.xlabel("Sum of the dice")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of sums ({len(results)} rolls)")

    os.makedirs("../plots", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"../plots/dice_distribution_{timestamp}.png"
    plt.savefig(filename)
    plt.close()
    print(f"Plot saved as {filename}")

if __name__ == "__main__":
    rolls = simulate_rolls()
    plot_results(rolls)
