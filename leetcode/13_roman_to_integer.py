class Solution:
    """
    Created     : Thu, 2020-Feb-27 18:47 
    Level       : Easy
    Description : Convert roman to decimal number.
    Assumption  : The roman number input is well-defined.
    """
    def romanToInt(self, s: str) -> int:
        res, prev = 0, 0
        mapping = { 'I':1,
                    'V':5, 
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000}
        for c in reversed(s): 
            if mapping[c] >= prev:
                # sum the value iff previous value same or more
                res += mapping[c]     
            else:
                # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc 
                res -= mapping[c]     
            prev = mapping[c]
        return res

import unittest
class TestRomanToInt(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_result(self):
        self.assertEqual(self.solution.romanToInt('III'), 3)
        self.assertEqual(self.solution.romanToInt('XX'), 20)
        self.assertEqual(self.solution.romanToInt('MCMXCIV'), 1994)
        self.assertEqual(self.solution.romanToInt('LVIII'), 58)
        self.assertEqual(self.solution.romanToInt('IX'), 9)
        self.assertEqual(self.solution.romanToInt('IV'), 4)
        self.assertEqual(self.solution.romanToInt('CM'), 900)
        self.assertEqual(self.solution.romanToInt('XC'), 90)

if __name__ == '__main__':
    unittest.main()
