class Solution:
    """
    Solved      :   
    Link        :   https://leetcode.com/problems/longest-substring-without-repeating-characters/
    Difficulty  :   Medium
    Description :   Given a string, find the length of the longest substring without repeating characters.
    """
    # TODO: replace set by array
    def lengthOfLongestSubstring(self, s: str) -> int:
        assert isinstance(s, str)
        length: int = len(s)
        alpha: set = set()
        i = j = longest = 0
        while i < length:
            if (length - i + j) <= longest: break
            c = s[i]
            if not c in alpha:
                alpha.add(c)
                j += 1
            else:
                longest = max(j, longest)
                i -= j
                j = 0
                alpha.clear()
            i += 1
        return max(j, longest)

import unittest
class TestConvert(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()

    def test_result(self) -> None:
        self.assertEqual(self.solution.lengthOfLongestSubstring('abcabcbb'), 3)
        self.assertEqual(self.solution.lengthOfLongestSubstring('bbbbb'), 1)
        self.assertEqual(self.solution.lengthOfLongestSubstring('pwwkew'), 3)
        self.assertEqual(self.solution.lengthOfLongestSubstring('abcabcbb abcde'), 6)
        self.assertEqual(self.solution.lengthOfLongestSubstring('1234    '), 5)
        self.assertEqual(self.solution.lengthOfLongestSubstring(''), 0)
        self.assertEqual(self.solution.lengthOfLongestSubstring('   '), 1)

    def test_type(self) -> None:
        with self.assertRaises(AssertionError):
            self.solution.lengthOfLongestSubstring(None)              # type: ignore

def debug() -> None:
    solution = Solution()
    solution.lengthOfLongestSubstring('pwwkew')

if __name__ == '__main__':
    unittest.main()
    # debug()
