class Solution:
    """
    Created     :   Fri, 2020-Feb-28 22:27 
    Difficulty  :   Medium
    Description :   Given an input string, reverse the string word by word.
    Link        :   https://leetcode.com/problems/reverse-words-in-a-string/
    Input       :   " hello world!   "
    Output      :   'world! hello' 
    """

    def pythonic_cheating_reverseWords(self, s: str) -> str:
        '''
            NOT RECOMMENDED.
            Very bad way for practicing algorithm purporse.
        '''
        return ''.join(s.split()[::-1])

    def reverseWords(self, s: str) -> str:
        '''
           Use 2 pointers start from the end of string.
                i: Loop through each char of string, also mark left-boundary of a word
                k: Mark the right-boundary of a word
        '''
        if len(s) <= 2: return s.strip()

        res: str = '' 
        i = k = len(s) - 1 
        while i >= 0:
            if ' ' == s[i]:
                if k != i:
                    if res == '':
                        res = res + s[i+1:k+1]
                    else:
                        res = res + ' ' + s[i+1:k+1]
                k = i-1 
            i -= 1

        if k != i:
            if res == '':
                return res + s[i+1:k+1]
            else:
                return res + ' ' + s[i+1:k+1]
        return res

       
import unittest
class TestConvert(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()

    def test_result(self) -> None:
        self.assertEqual(self.solution.reverseWords('the sky is blue'), 'blue is sky the')
        self.assertEqual(self.solution.reverseWords('  hello  world!  '), 'world! hello')
        self.assertEqual(self.solution.reverseWords(' 888 999 '), '999 888')
        self.assertEqual(self.solution.reverseWords(' #$% *  '), '* #$%')
        self.assertEqual(self.solution.reverseWords('    '), '')
        self.assertEqual(self.solution.reverseWords('hi!'), 'hi!')


if __name__ == '__main__':
    unittest.main()
