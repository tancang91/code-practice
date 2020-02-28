class Solution:
    """
    Created     :   Thu, 2020-Feb-27 22:58
    Difficulty  :   Medium
    Description :   The string "PAYPALISHIRING" is written in a zigzag pattern 
                    on a given number of rows like this: (you may want to display 
                    this pattern in a fixed font for better legibility) 
    
    input       :   "PAYPALISHIRING"
    Output      :   P   A   H   N
                    A P L S I I G
                    Y   I   R 
    """
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or numRows >= len(s): return s

        arr: list = []
        i = count = 0
        length = len(s)

        while count < length:
            while count < length and i < numRows:
                arr.append((i, s[count]))
                count += 1
                i += 1
            
            i -= 2
            while count < length and i > 0:
                arr.append((i, s[count]))
                count += 1
                i -= 1

        # TODO: Find the way to remove sort
        arr = sorted(arr, key= lambda x: x[0])
        arr = [c[1] for c in arr]
        return ''.join(arr) 
        
# python3 -m unittest -v 6_zigzag_conversion.py
import unittest
class TestConvert(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_result(self):
        self.assertEqual(self.solution.convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')
        self.assertEqual(self.solution.convert('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')
        self.assertEqual(self.solution.convert('PAYPALISHIRING', 100), 'PAYPALISHIRING')
        self.assertEqual(self.solution.convert('AB', 1), 'AB')

if __name__ == '__main__':
    unittest.main()
