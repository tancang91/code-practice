INT_MAX: int = (1 << 31) - 1
INT_MIN: int = ~(1 << 31) + 1

class Solution:
    """
    Created     : Wed, 2020-Feb-26 00:00 
    Level       : Medium
    Description : Convert string to integer.
    """
    def myAtoi(self, str_input: str) -> int:
        if not isinstance(str_input, str):
            return 0

        trim_str: str = str_input.lstrip()
        length = len(trim_str)
        if length == 0: return 0

        INT_MAX: int = (1 << 31) - 1
        INT_MIN: int = ~(1 << 31) + 1
        total: int = 0
        sign: int = -1 if '-' == trim_str[0] \
                    else 1

        for i in range(length):
            char = trim_str[i]
            if i == 0 and ('-' == char or '+' == char):
                continue
            
            # Unicode number range [48-58] -> [0-9]
            ord_int:int = ord(char) - 48
            if 0 <= ord_int <= 9:
                # This step to ensure total value not integer-overflow
                # INT_MIN <= total*10 + digit <= INT_MAX
                upper_limit: int = int((INT_MAX-ord_int)/10)
                if sign == 1 and total > upper_limit:
                    return INT_MAX
                elif sign == -1 and (total*sign) < int((INT_MIN + ord_int)/10):
                    return INT_MIN
                total = total*10 + ord_int
            else: break

        return total * sign
    
    # TODO: Trim whitespace
    @staticmethod
    def trim_begin(str_input: str) -> str:
        trim_str: str = str_input
        return trim_str 
        
import unittest
class TestMyAtoi(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()

    def test_result(self) -> None:
        self.assertEqual(self.solution.myAtoi('6996'), 6996)
        self.assertEqual(self.solution.myAtoi('+12345'), 12345)
        self.assertEqual(self.solution.myAtoi('-12345'), -12345)
        self.assertEqual(self.solution.myAtoi('    12345'), 12345)
        self.assertEqual(self.solution.myAtoi('12345 stupid string'), 12345)
        self.assertEqual(self.solution.myAtoi('  stupid string 12345'), 0)
        self.assertEqual(self.solution.myAtoi('-91283472332'), INT_MIN)
        self.assertEqual(self.solution.myAtoi('91283472332'), INT_MAX)
        self.assertEqual(self.solution.myAtoi('--1'), 0)
        self.assertEqual(self.solution.myAtoi('++1'), 0)
        self.assertEqual(self.solution.myAtoi(''), 0)
        self.assertEqual(self.solution.myAtoi(str(INT_MAX)), INT_MAX)

if __name__ == '__main__':
    unittest.main()

