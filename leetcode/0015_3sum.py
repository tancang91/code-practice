from typing import List

class Solution:
    """
    Solved      :   
    Link        :   https://leetcode.com/problems/3sum/ 
    Difficulty  :   Medium
    """
    def threeSum__(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        sums: int = 0
        complement = [sums-x for x in nums]
        length: int = len(nums)

        for i in range(length):
            pool: set = set()
            for j in range(i, length):
                if i == j: continue
                if nums[j] in pool:
                    res.append([nums[i], nums[j], sums-nums[i]-nums[j]])
                    break
                pool.add(complement[i]-nums[j])
        return res

    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res


import unittest
class TestConvert(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()

    def test_result(self) -> None:
        self.assertEqual(self.solution.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])
        self.assertEqual(self.solution.threeSum([2, -1, -4, 10]), [[]])
        

def debug() -> None:
    solution = Solution()
    l = solution.threeSum([-1, 0, 1, 2, -1, -4])
    print(l)

if __name__ == '__main__':
    # unittest.main()
    debug()
