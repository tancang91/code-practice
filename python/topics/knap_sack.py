class Solution:
    '''
    dp table as below
    +----------------------------------------+
        | 0 | 1 | 2 | .. | Weight_constraint
    0   | 
    w1  |
    w2  |
    ... |
    wn  |

    '''

    def knap_sack(self, weigh: list, val: list, W: int) -> int:
        N: int = len(weigh)
        assert N == len(val)

        dp: list = self._create_matrix(N+1,W+1)

        for i in range(0, N+1):
            for j in range(0, W+1):
                if i == 0 or j==0:
                    dp[i][j] = 0
                elif j < weigh[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    cur: int = val[i-1] + dp[i-1][j-weigh[i-1]]
                    dp[i][j] = max(cur, dp[i-1][j])
        return dp[N][W]

    @staticmethod
    def _create_matrix(rows: int, cols: int) -> list:
        return [[None for _ in range(cols)] for _ in range(rows)]

import unittest
class TestConvert(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()

    def test_result(self) -> None:
        pass


def debug():
    solution = Solution()
    weigh = [3, 2, 1]
    val = [120, 100, 60]
    W = 5
    max_val: int = solution.knap_sack(weigh, val, W)
    print(max_val)

if __name__ == '__main__':
    # unittest.main()
    debug()

