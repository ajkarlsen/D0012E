from algorithm import sortStack

import numpy as np
import matplotlib.pyplot as plt


def generatePlotData(start, end, steps):
    x = np.arange(start, end + steps, steps)
    y = []
    for n in x:
        print(f"Running sortStack({n})...")
        runtime = sortStack(n)
        y.append(runtime)
    return x, np.array(y)

def plot_results(x, y):
    plt.style.use('bmh')
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x, y, marker='o', linewidth=2, color='royalblue')
    ax.set_title("Runtime of sortStack()")
    ax.set_xlabel("Input Size (n)")
    ax.set_ylabel("Runtime (seconds)")


    sample_indices = np.linspace(0, len(x)-1, min(10, len(x)), dtype=int)
    table_data = [[f"{x[i]:,}", f"{y[i]:.6f}"] for i in sample_indices]
    column_labels = ['Input Size (n)', 'Runtime (s)']


    table = plt.table(
        cellText=table_data,
        colLabels=column_labels,
        loc='right',
        cellLoc='center'
    )

    plt.subplots_adjust(right=0.75)
    plt.savefig("sorted.png", dpi=300, bbox_inches='tight')
    plt.show()

x, y = generatePlotData(0, 100000, 10000)
plot_results(x, y)