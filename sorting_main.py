import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns

#create random array 
low = 1
high = 1000
size = 5  #1000

# low <= randint <= high-1 (aka max = high-1)
rand_array = np.random.randint(low, high, size) 
np.random.shuffle(rand_array)

np.random.seed(6969) 

x = np.arange(0, size, 1)
fig, ax = plt.subplots() 
ax.bar(x, rand_array, align="edge", width=0.8)


sorting_algo = "Selection"
def SelectionSort1(arr): 
    for i in range(len(arr)): 
        for j in range(i+1,len(arr)): 
            plt.bar(x, rand_array)
            plt.pause(1)
            plt.clf()

            if arr[i] > arr[j]: 
                arr[i], arr[j] = arr[j], arr[i]
    plt.show()
    ax.set(xlabel="Index", ylabel="Value", title=f"{sorting_algo} sort")
    return arr

def SelectionSort2(arr): 
    for i in range(len(arr)): 
        min_idx = i
        for j in range(i+1,len(arr)): 
            plt.bar(x, rand_array)
            plt.pause(0.01)
            plt.clf()
            if arr[i] > arr[j]: 
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    plt.show()
    return arr

def InsertionSort(arr): 
    for i in range(len(arr)): 
        chosen_ele = arr[i]
        location = i 
        while location > 0 and arr[location - 1] > chosen_ele: 
            arr[location] = arr[location-1]
            location = location-1
        arr[location] = chosen_ele
    return arr

def merge(arr, l, m, r): 
    # merges two subarrays of arr
    n1 = m - l + 1  
    n2 = r - m 

    tmpL = [0]*(n1)
    tmpR = [0]*(n2)

    for i in range(0, n1): 
        tmpL[i] = arr[l+i]
    for j in range(0,n2): 
        tmpR[j] = arr[m + 1 + j]

    # merge temps into main arr
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2: 
        if tmpL[i] <= tmpR[j]: 
            arr[k] = tmpL[i]
            i += 1
        else: 
            arr[k] = tmpR[j]
            j+=1
        k+=1 

    while i < n1:
        arr[k] = tmpL[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = tmpR[j]
        j += 1
        k += 1

    return arr

def MergeSort(arr, l, r): 
    if l < r: 
        m = l+(r-l)//2
        MergeSort(arr, l, m)
        MergeSort(arr, m+1, r)
        merge(arr, l, m, r)
    return arr

def partition(arr, low, high): 
    piv = arr[high]
    i = low-1
    for j in range(low, high): 
        if  arr[j] <= piv: 
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def QuickSort(arr, low, high): 
    if low < high: 
        par = partition(arr, low, high)
        QuickSort(arr, low, par - 1)
        QuickSort(arr,  par + 1, high)
    return arr 

def heapify(arr, N, i): 
    largest = i # largest = root
    l = 2*i + 1
    r = 2*i + 2

    # if left node exists and is bigger than root -> swap l and root
    if l < N and arr[largest] < arr[l]: 
        largest = l
    
    # ifi right node exists and is bigger than root -> swawp r and root
    if r < N and arr[largest] < arr[r]: 
        largest = r 
    
    #change root if needed
    if largest != i: 
        arr[largest], arr[i] = arr[i], arr[largest]
        
        #heapify the new root
        heapify(arr, N, largest)
    
def HeapSort(arr): 
    N = len(arr)
    for i in range(N//2 - 1, -1, -1): 
        heapify(arr, N, i)
    
    for i in range(N-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr 

def BubbleSort(arr): 
    for i in range(len(arr)): 
        for j in range(0, len(arr)-i-1): 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr  

SelectionSort1(rand_array)