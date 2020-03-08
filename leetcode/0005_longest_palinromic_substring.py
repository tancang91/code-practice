class Solution:
    """
    Solved      :   
    Link        :   https://leetcode.com/problems/longest-palindromic-substring/
    Difficulty  :   Medium
    Description :   Given a string s, find the longest palindromic substring in s.
    """
    # TODO: Dynamic programming
    def longestPalindrome(self, s: str) -> str:
        assert isinstance(s, str)
        length: int = min(len(s), 1000)
        if length < 2: return s

        longest_palin: str = s[0]
        for i in range(length):
            for j in range(length-1, i, -1):
                if len(longest_palin) >= (j-i+1):
                    break
                if self.check_palin(s, i, j):
                    temp = s[i:j+1]
                    if len(longest_palin) < len(temp):
                        longest_palin = temp
                    break
        return longest_palin

    def check_palin(self, s: str,i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        return True

import unittest
class TestConvert(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()

    def test_result(self) -> None:
        self.assertEqual(self.solution.longestPalindrome('babad'), 'bab')
        self.assertEqual(self.solution.longestPalindrome('cbbd'), 'bb')
        self.assertEqual(self.solution.longestPalindrome('abcd'), 'a')
        self.assertEqual(self.solution.longestPalindrome('  abcd'), '  ')
        self.assertEqual(self.solution.longestPalindrome('ds   fgh'), '   ')
        self.assertEqual(self.solution.longestPalindrome('a'), 'a')
        self.assertEqual(self.solution.longestPalindrome('abb'), 'bb')

    def test_type(self) -> None:
        with self.assertRaises(AssertionError):
            self.solution.longestPalindrome(None)              # type: ignore

if __name__ == '__main__':
    unittest.main()

