from typing import List

class Solution:
    """
    Solved      :   Wed, 2020-Mar-11 11:16 
    Link        :   https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/ 
    Difficulty  :   Medium
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = last = -1
        low = 0
        high = len(nums) - 1
        while high >= low:
            mid = low + (high-low)//2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                first = last = mid
                break

        if first == -1: return [-1, -1]
        first -= 1; last += 1
        while first >= low or last <= high:
            if first >= low and nums[first] == target:
                first -= 1
            else: low = first + 1

            if last <= high and nums[last] == target:
                last += 1
            else: high = last - 1
        return [first + 1, last - 1]

import unittest
class TestConvert(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()

    def test_result(self) -> None:
        self.assertEqual(self.solution.searchRange([5,7,7,8,8,10], 8), [3,4])
        self.assertEqual(self.solution.searchRange([5,7,7,8,8,10], 6), [-1,-1])
        self.assertEqual(self.solution.searchRange([1,1,1,1,1,1], 1), [0,5])
        self.assertEqual(self.solution.searchRange([1,2,3,4,5,6], 1), [0,0])
        self.assertEqual(self.solution.searchRange([1,2,3,4,5,6], 6), [5,5])

def debug() -> None:
    solution = Solution()
    solution.searchRange([5,7,7,8,8,10], 8)

if __name__ == '__main__':
    unittest.main()
    # debug()
