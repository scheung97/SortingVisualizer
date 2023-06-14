import sorting_algos as sa
import matplotlib.pyplot as plt
import numpy as np
import time 

DEBUG_MODE = 1

def visualize_sorting(data,sorting_algo): 
    #sort data
    try:
        sorted_data = sorting_algo(data)
        return sorted_data
    except Exception as e:
        print(e)

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
    sorted_data = visualize_sorting(rand_array, sa.QuickSort(rand_array,0, len(rand_array)-1))
    # print(sorted_data)
    plt.close('all')