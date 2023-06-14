import sorting_algos as sa
import matplotlib.pyplot as plt
import numpy as np
import time 

DEBUG_MODE = 1

def visualize_sorting(data,sorting_algo): 
    #sort data
    algo = sorting_algo.lower() 

    if algo == "selectionsort1": 
        sorted_data = sa.SelectionSort1(data)
    
    elif algo ==  "selectionsort2": 
        sorted_data = sa.SelectionSort2(data) 
    
    elif algo ==  "insertionsort1": 
        sorted_data = sa.InsertionSort(data) 
    
    elif algo ==  "mergesort": 
        sorted_data = sa.MergeSort(data, 0, len(data)-1)
    
    elif algo ==  "quicksort": 
        sorted_data = sa.QuickSort(data,0,len(data)-1) 
    
    elif algo ==  "heapsort": 
        sorted_data = sa.HeapSort(data) 
    
    elif algo ==  "bubblesort": 
        sorted_data = sa.BubbleSort(data)
    else: 
        sorted_data = "Command not recognized."
        # print("Command not recognized.")
        
    return sorted_data 


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
    sorted_data = visualize_sorting(rand_array.copy(), "QuickSort")
    print(sorted_data)
    plt.close('all')