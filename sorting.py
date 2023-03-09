import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns

#create random array 
low = 1
high = 1000
size = 5  #1000

# low <= randint <= high-1 (aka max = high-1)
rand_array = np.random.randint(low, high, size) 

def SelectionSort1(arr): 
    for i in range(len(arr)): 
        for j in range(i+1,len(arr)): 
            if arr[i] > arr[j]: 
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def SelectionSort2(arr): 
    for i in range(len(arr)): 
        min_idx = i
        for j in range(i+1,len(arr)): 
            if arr[i] > arr[j]: 
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

