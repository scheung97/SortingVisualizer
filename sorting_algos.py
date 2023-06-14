import matplotlib.pyplot as plt

def SelectionSort1(arr): 
    for i in range(len(arr)): 
        for j in range(i+1,len(arr)): 
            if arr[i] > arr[j]: 
                # Highlight current swap 
                plt.clf() 
                colors = ['blue'] * len(arr)
                colors[i] = 'red'
                colors[j] = 'red'
                plt.bar(range(len(arr)), arr, color = colors)
                plt.pause(0.5)

                # Swap elements
                arr[i], arr[j] = arr[j], arr[i]

            # Highlight steps between swaps 
            plt.clf() 
            colors = ['blue'] * len(arr)
            colors[i] = 'red'
            colors[j] = 'red'
            plt.bar(range(len(arr)), arr, color = colors)
            plt.pause(0.5)
            colors[i] = 'blue'
            colors[j] = 'blue'
            plt.bar(range(len(arr)), arr, color = colors)         
    return arr

def SelectionSort2(arr): 
    for i in range(len(arr)): 
        min_idx = i
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j
        
        if min_idx != i: 
            # Highlight current swap 
            plt.clf() 
            colors = ['blue'] * len(arr)
            colors[i] = 'red'
            colors[min_idx] = 'red'
            plt.bar(range(len(arr)), arr, color = colors)
            plt.pause(0.5)

            # Swap elements
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # Highlight steps between swaps 
        plt.clf() 
        colors = ['blue'] * len(arr)
        colors[i] = 'red'
        colors[min_idx] = 'red'
        plt.bar(range(len(arr)), arr, color = colors)
        plt.pause(0.5)
    return arr

#need to update this 
def InsertionSort(arr): 
    for i in range(1,len(arr)): 
        chosen_ele = arr[i]
        location = i-1 

        while location >= 0 and arr[location] > chosen_ele: 
            arr[location+1] = arr[location]
            location -= 1

            # Update plot
            plt.clf()
            bars = plt.bar(range(len(arr)), arr, color = 'blue')
            bars[location+1].set_color('red')
            bars[i].set_color('red')
            plt.pause(2)
            bars[location].set_color('blue')
            bars[i].set_color('blue')
            
        arr[location+1] = chosen_ele
        plt.clf()
        bars = plt.bar(range(len(arr)), arr, color = 'blue')
        bars[location+1].set_color('red')
        bars[i].set_color('red')
        plt.pause(2)
        bars[location].set_color('blue')
        bars[i].set_color('blue')

        # Update plot
        plt.clf()
        plt.bar(range(len(arr)), arr, color = 'blue')
        plt.pause(0.05)
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
        
        #update plot
        plt.clf()
        bars = plt.bar(range(len(arr)), arr, color='blue')
        for i in range(l, m + 1):
            bars[i].set_color('red')
        for i in range(m + 1, r + 1):
            bars[i].set_color('green')
        plt.pause(1)

        #Recursively sort
        MergeSort(arr, l, m)
        MergeSort(arr, m+1, r)
        merge(arr, l, m, r)

        #update plot
        plt.clf()
        bars = plt.bar(range(len(arr)), arr, color='blue')
        for i in range(l, m + 1):
            bars[i].set_color('red')
        for i in range(m + 1, r + 1):
            bars[i].set_color('green')
        plt.pause(1)

        for i in range(l, r + 1):
            bars[i].set_color('blue')
        plt.pause(1)

    return arr

def partition(arr, low, high): 
    piv = arr[high]
    i = low-1
    for j in range(low, high): 
        if  arr[j] <= piv: 
            i=i+1

            #update plot 
            plt.clf() 
            colors = ['blue'] * len(arr)
            colors[i] = 'red'
            colors[j] = 'red'
            plt.bar(range(len(arr)), arr, color = colors)
            plt.pause(0.5)

            (arr[i], arr[j]) = (arr[j], arr[i])
        
        # update plot
        plt.clf() 
        colors = ['blue'] * len(arr)
        colors[j] = 'red'
        colors[high] = 'red'
        plt.bar(range(len(arr)), arr, color = colors)
        plt.pause(0.5)

    # update plot
    plt.clf() 
    colors = ['blue'] * len(arr)
    colors[i+1] = 'red'
    colors[high] = 'red'
    plt.bar(range(len(arr)), arr, color = colors)
    plt.pause(0.5)


    (arr[i+1], arr[high]) = (arr[high], arr[i+1])  
    
    # update plot
    plt.clf() 
    colors = ['blue'] * len(arr)
    plt.bar(range(len(arr)), arr, color = colors)
    plt.pause(0.5)

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
                # Highlight current swap
                plt.clf() 
                colors = ['blue'] * len(arr)
                colors[j] = 'red'
                colors[j+1] = 'red'
                plt.bar(range(len(arr)), arr, color = colors)
                plt.pause(0.5)

                # Swap elements
                arr[j], arr[j+1] = arr[j+1], arr[j]

            # Highlight steps between swaps 
            plt.clf() 
            colors = ['blue'] * len(arr)
            colors[j] = 'red'
            colors[j+1] = 'red'
            plt.bar(range(len(arr)), arr, color = colors)
            plt.pause(0.5)
            colors[j] = 'blue'
            colors[j+1] = 'blue'
            plt.bar(range(len(arr)), arr, color = colors)

    return arr  
