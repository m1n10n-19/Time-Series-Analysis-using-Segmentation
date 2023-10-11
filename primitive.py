import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

primitives = {
    'A': [1.0, 1.0, 1.0],
    'B': [1.0, 2.0, 4.0],
    'C': [1.0, 2.0, 3.0],
    'D': [1.0, 3.0, 4.0],
    'E': [4.0, 2.0, 1.0],
    'F': [3.0, 2.0, 1.0],
    'G': [4.0, 3.0, 1.0],
    'H': [2.0, 4.0, 2.0],
    'I': [3.0, 1.0, 3.0]
}

def plot_primitive(ax, primitive, x_vals):
    y_vals = primitives[primitive]
    if len(x_vals) > 2:
        cs = CubicSpline(x_vals, y_vals, bc_type='natural')
        x_vals_smooth = np.linspace(min(x_vals), max(x_vals), 1000)
        y_vals_smooth = cs(x_vals_smooth)
        ax.plot(x_vals_smooth, y_vals_smooth, label=primitive)
    else:
        ax.plot(x_vals, y_vals, 'o-', label=primitive)
    ax.set_ylim([0.0, 5.0])
    ax.set_xlim([0.0, 4.0])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

def plot_primitives(primitives):
    x_vals = [1, 2, 3]  
    
    num_primitives = len(primitives)
    num_cols = 3
    num_rows = (num_primitives + num_cols - 1) // num_cols
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(15, 5 * num_rows))

    for idx, (primitive, ax) in enumerate(zip(primitives.keys(), axs.flatten())):
        plot_primitive(ax, primitive, x_vals)
        ax.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    plot_primitives(primitives)
