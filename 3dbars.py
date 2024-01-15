import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_data():
    # Generate sample data for demonstration
    x = np.arange(5)  # X-axis categories
    y = np.arange(4)  # Y-axis categories
    x, y = np.meshgrid(x, y)

    # Data for three datasets
    data1 = np.array([[1, 2, 3, 4, 5],
                      [2, 3, 4, 5, 6],
                      [3, 4, 5, 6, 7],
                      [4, 5, 6, 7, 8]])

    data2 = np.array([[2, 3, 4, 5, 6],
                      [3, 4, 5, 6, 7],
                      [4, 5, 6, 7, 8],
                      [5, 6, 7, 8, 9]])

    data3 = np.array([[3, 4, 5, 6, 7],
                      [4, 5, 6, 7, 8],
                      [5, 6, 7, 8, 9],
                      [6, 7, 8, 9, 10]])

    return x, y, data1, data2, data3

def plot_3d_bars(ax, x, y, data, color, label):
    ax.bar3d(x.flatten(), y.flatten(), np.zeros_like(x).flatten(), 0.8, 0.8, data.flatten(), shade=True, color=color, label=label)

def main():
    # Generate data
    x, y, data1, data2, data3 = generate_data()

    # Create a 3D subplot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot each dataset
    plot_3d_bars(ax, x, y, data1, color='r', label='Dataset 1')
    plot_3d_bars(ax, x, y, data2, color='g', label='Dataset 2')
    plot_3d_bars(ax, x, y, data3, color='b', label='Dataset 3')

    # Customize the plot
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Complex 3D Bar Chart')
    ax.legend()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
