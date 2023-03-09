import numpy as np

import unittest
from sorting import SelectionSort1, SelectionSort2
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
    
    




if  __name__ ==  "__main__": 
    unittest.main()