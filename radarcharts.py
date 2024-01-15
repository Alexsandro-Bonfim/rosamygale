import numpy as np
import matplotlib.pyplot as plt

def radar_chart(ax, categories, values, title):
    # Number of variables/categories
    num_vars = len(categories)

    # Compute angle of each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Repeat the first value to close the circular plot
    values += values[:1]
    angles += angles[:1]

    # Plot the values
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=title)
    ax.fill(angles, values, alpha=0.4)

    # Add labels
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    # Add a title
    ax.set_title(title, size=20, color='gray', y=1.1)

def main():
    # Define the categories and values for each dataset
    categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
    
    values1 = [4, 3, 4, 2, 5]
    values2 = [3, 2, 5, 1, 4]

    # Create a figure and a set of subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 6), subplot_kw=dict(polar=True))

    # Create radar charts for each dataset
    radar_chart(axs[0], categories, values1, 'Dataset 1')
    radar_chart(axs[1], categories, values2, 'Dataset 2')

    # Add a legend
    axs[1].legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()

