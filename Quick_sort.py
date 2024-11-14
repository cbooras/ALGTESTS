def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

import unittest

class TestQuickSort(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(quick_sort([3, 1, 4, 1, 5, 9, 2]), [1, 1, 2, 3, 4, 5, 9])

    def test_invalid_data_type(self):
        with self.assertRaises(TypeError):
            quick_sort(["string", 1, 2, 3])

    def test_large_array(self):
        large_array = list(range(1000, 0, -1))
        sorted_array = list(range(1, 1001))
        self.assertEqual(quick_sort(large_array), sorted_array)

    def test_boundary_cases(self):
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(quick_sort([42]), [42])
        self.assertEqual(quick_sort([3, 3, 3]), [3, 3, 3])
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_idempotency(self):
        array = [2, 1, 3, 4, 5]
        self.assertEqual(quick_sort(quick_sort(array)), [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()
