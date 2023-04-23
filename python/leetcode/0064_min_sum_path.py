from typing import List

class Solution:
    """
    Solved      :   Wed, 2020-Mar-11 14:27 
    Link        :   https://leetcode.com/problems/minimum-path-sum/
    Difficulty  :   Medium
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_len: int = len(grid)
        col_len: int = len(grid[0])
        if row_len == 1 and col_len == 1: return grid[0][0]

        dp = {}
        dp[(0,0)] = grid[0][0] 
        
        for k in range(1,row_len):
            dp[(k,0)] = dp[(k-1,0)] + grid[k][0]
        for k in range(1,col_len):
            dp[(0,k)] = dp[(0,k-1)] + grid[0][k]

        i = j = 1
        while i < row_len and j < col_len:
            for k in range(min(i,row_len), row_len):
                dp[(k,j)] = grid[k][j] + min(dp[(k-1,j)], dp[(k,j-1)])
            for k in range(min(j,col_len), col_len):
                dp[(i,k)] = grid[i][k] + min(dp[(i-1,k)], dp[(i,k-1)])
            i += 1; j += 1
        
        return dp[(row_len-1,col_len-1)]

    def minPathSum_cleaner(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        row_len, col_len = len(grid), len(grid[0])
        dp = [grid[0][0]]

        for col in range(1, col_len):
            dp.append(dp[col-1]+grid[0][col])

        for row in range(1, row_len):
            dp[0] = dp[0]+grid[row][0]
            for col in range(1, col_len):
                dp[col] = min(dp[col-1], dp[col])+grid[row][col]

        return dp[-1]


import unittest
class TestConvert(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()

    def test_result(self) -> None:
        self.assertEqual(self.solution.minPathSum([[1,3,1], [1,5,1], [4,2,1]]), 7)
        self.assertEqual(self.solution.minPathSum([[1,3,1]]), 5)
        self.assertEqual(self.solution.minPathSum([[1], [2], [3]]), 6)
        self.assertEqual(self.solution.minPathSum([[1]]), 1)
        

def debug() -> None:
    solution = Solution()
    i = solution.minPathSum([[1,3,1], [1,5,1], [4,2,1]])
    return i

if __name__ == '__main__':
    unittest.main()
