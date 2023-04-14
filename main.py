import sorting_algos as sa
import matplotlib.pyplot as plt
import numpy as np
import time 

DEBUG_MODE = 1

def visualize_sorting(data,size): 
    #create chart
    # x = np.arange(0, size, 1)
    # fig, ax = plt.subplots() 
    # ax.bar(x, rand_array, align="edge", width=0.8)
    plt.bar(range(len(data)), data)
    plt.draw()
    plt.pause(1)


    #sort data
    sorted_data = sa.SelectionSort1(data)

    #display sorted data 
    plt.clf()
    plt.bar(range(len(sorted_data)), sorted_data)
    plt.draw()
    plt.pause(1)
    pass 

if __name__ == "__main__": 
    # For consistant array when debugging
    if DEBUG_MODE == 1: 
        np.random.seed(6969)

    # Generate random data:
    low = 1
    high = 1000
    size = 5  #1000
    
    rand_array = np.random.randint(low, high, size)  # low <= randint <= high-1 (aka max = high-1)
    np.random.shuffle(rand_array)  # Shuffle the array
    print(f"Input Data: {rand_array}")
    
    # Visualize sort
    visualize_sorting(rand_array, size)
    
