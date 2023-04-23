class Solution:

    def stair_case(self, steps: list, target: int):
        state: list = [1000000] * (target+1)
        l: list = [[] for _ in range(target+1)]
        state[0] = 0

        for i in range(1, target+1):
            res: list = []
            for e in steps:
                if e <= i:
                    if len(l[i-e]) >= len(l[i]):
                        l[i] = list(l[i-e])
                        l[i].append(e)

                        res.append(l[i])
        return state[target], res

    def stair_case2(self, steps: list, target: int):
        state: list = [None for _ in range(target+1)]
        state[0] = []
        for i in range(1, target+1):
            for e in steps:
                if e <= i:
                    pass

def debug() -> None:
    solution: Solution = Solution()
    s, l = solution.stair_case([2,3,5], 8)

if __name__ == '__main__':
    debug()
