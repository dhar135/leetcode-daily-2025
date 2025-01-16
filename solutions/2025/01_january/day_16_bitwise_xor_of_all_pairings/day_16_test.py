import unittest
from .day_16_solution import Solution


class MyTestCase(unittest.TestCase):
    def test_example1(self, solution=Solution()):
        nums1, nums2 = [2, 1, 3], [10, 2, 5, 0]
        expected = 13
        self.assertEqual(solution.xorAllNums(nums1, nums2), expected)

    def test_example2(self, solution=Solution()):
        nums1, nums2 = [1, 2], [3, 4]
        expected = 0
        self.assertEqual(solution.xorAllNums(nums1, nums2), expected)


if __name__ == '__main__':
    unittest.main()
