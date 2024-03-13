import os
import numpy as np
import matplotlib.pyplot as plt
# from cellular_automata.prototype_wind import sigmoid
from cellular_automata.prototype_wind import norm




def sigmoid(x, k):
    x= norm(x)
    return 1 / (1 + np.exp(-k * x))

# Values of k for the sigmoid curves
k_values = [0.9, 1.1, 1.3, 1.5, 1.75]

# Generate x values
x = np.linspace(0, 4, 100)



if __name__ == '__main__':

    # Plot the sigmoid curves
    for k in k_values:
        y = sigmoid(x, k)
        plt.plot(x, y, label=f'k = {k}')

    # Add labels and a legend
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()


    image_name = f"sigmoid_norm.png"
    
    current_dir = os.getcwd()
    data_folder_path = os.path.join(current_dir, "data")
    folder_path = os.path.join(data_folder_path, "sigmoid")
    image_path = os.path.join(folder_path, image_name)


    if not os.path.exists(folder_path):
                os.makedirs(folder_path)


    plt.savefig(image_path)

    # Display the plot
    plt.show()