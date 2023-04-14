import numpy as np
import unittest
from sorting_algos import *

def createArray(): 
        low = 1,
        high = 1_000,
        size = 5  #1000

        # low <= randint <= high-1 (aka max = high-1)
        rand_array = np.random.randint(low, high, size) 
        return rand_array 

arr = createArray()


class TestSorting(unittest.TestCase): 
    def test_selection_sort(self): 
        global arr
        actual = SelectionSort1(arr)
        expected = sorted(arr)
        self.assertEqual(actual.tolist(), expected)#, f"Should be: {sorted(arr)}")

    def test_selection_sort2(self): 
        global arr
        actual = SelectionSort2(arr)
        expected = sorted(arr)
        self.assertEqual(actual.tolist(), expected)#, f"Should be: {sorted(arr)}")

    
    def test_insertion_sort(self): 
        global arr
        actual = InsertionSort(arr)
        expected = sorted(arr)
        self.assertEqual(actual.tolist(), expected)#, f"Should be: {sorted(arr)}")
   
    def test_merge_sort(self): 
        global arr
        actual = MergeSort(arr,l=0, r = len(arr)-1)
        expected = sorted(arr)
        self.assertEqual(actual.tolist(), expected)#, f"Should be: {sorted(arr)}")
    
    def test_quick_sort(self): 
        global arr
        actual = QuickSort(arr, low = 0, high = len(arr)-1)
        expected = sorted(arr)
        self.assertEqual(actual.tolist(), expected)#, f"Should be: {sorted(arr)}")
    
    def test_heap_sort(self): 
        global arr
        actual = HeapSort(arr)
        expected = sorted(arr)
        self.assertEqual(actual.tolist(), expected)#, f"Should be: {sorted(arr)}")
    
    def test_bubble_sort(self): 
        global arr
        actual = BubbleSort(arr)
        expected = sorted(arr)
        self.assertEqual(actual.tolist(), expected)#, f"Should be: {sorted(arr)}")

if  __name__ ==  "__main__": 
    unittest.main()