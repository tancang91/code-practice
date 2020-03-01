class Solution:
    """
    Solved      :   Sun, 2020-Mar-01 15:56 
    Link        :   https://leetcode.com/problems/reverse-words-in-a-string/ 
    Difficulty  :   Medium
    Description :   Write a function to check whether an input string is a valid 
                    IPv4 address or IPv6 address or neither.
    """
    def validIPAddress(self, IP: str) -> str: 
        assert isinstance(IP, str) 
        ip_strip: str = IP.strip()
        length: int = len(ip_strip)
        if length < 7 or length > 39:
            return 'Neither'
        
        # k: first index of ip address field.
        # count: count number of character '.' or ':' in address
        #     k
        # 123.123.11.3
        k = count = 0
        is_ipv4: bool = False
        is_first_time: bool = True
        for i in range(length):
            c = ip_strip[i].upper()
            if c not in '0123456789ABCDEF':
                if '.' == c or ':' == c:
                    if '.' == c and (is_ipv4 or is_first_time) and i != k:
                        field: str = ip_strip[k:i]
                        if not self.is_ipv4_filed_valid(field):
                            return 'Neither'
                        is_ipv4 = True

                    elif ':' == c and (not is_ipv4 or is_first_time) and i != k:
                        if not 1 <= (i-k) <= 4:
                            return 'Neither'
                        is_ipv4 = False
                    else:
                        return 'Neither'
            
                    k = i+1
                    count += 1
                    is_first_time = False
                else:
                    return 'Neither'

        if count == 3 and is_ipv4 and self.is_ipv4_filed_valid(ip_strip[k:length]): 
            return 'IPv4'
        elif count == 7 and not is_ipv4 and 1 <= (length -k) <= 4:
            return 'IPv6'
        else: return 'Neither'

    @staticmethod
    def is_ipv4_filed_valid(s: str) -> bool:
        length = len(s)
        if not 1 <= length <= 3 or \
            not s.isnumeric() or \
            ('0' == s[0] and length > 1) or \
            not 0 <= int(s) <= 255:
                return False

        return True


       
import unittest
class TestConvert(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()

    def test_result(self) -> None:
        self.assertEqual(self.solution.validIPAddress('172.16.254.1'), 'IPv4')
        self.assertEqual(self.solution.validIPAddress('01.01.01.01'), 'Neither')
        self.assertEqual(self.solution.validIPAddress(
                            '192.0.0.1'), 'IPv4')
        self.assertEqual(self.solution.validIPAddress('1.1.1.01'), 'Neither')
        self.assertEqual(self.solution.validIPAddress(
                            '2001:0db8:85a3:0:0:8A2E:0370:7334'), 'IPv6')
        self.assertEqual(self.solution.validIPAddress(
                            '2001:0db8:85a3:0000:0000:8A2E:0370:7334'), 'IPv6')
        self.assertEqual(self.solution.validIPAddress('256.256.256.256'), 'Neither')
        self.assertEqual(self.solution.validIPAddress('134.111.2.3.4'), 'Neither')
        self.assertEqual(self.solution.validIPAddress('ff:ff:ff:ff:aa'), 'Neither')
        self.assertEqual(self.solution.validIPAddress('some stupid string'), 'Neither')
        self.assertEqual(self.solution.validIPAddress(
                            '02001:0db8:85a3:0000:0000:8a2e:0370:7334'), 'Neither')
        self.assertEqual(self.solution.validIPAddress(
                            '200.123:85a3:0000:0000:8a2e:0370:7334'), 'Neither')
        self.assertEqual(self.solution.validIPAddress(
                            '1e1.1.1.1'), 'Neither')
        self.assertEqual(self.solution.validIPAddress(
                            '192.0.0.256'), 'Neither')
        self.assertEqual(self.solution.validIPAddress(
                            '12..3.4'), 'Neither')

    def test_type(self) -> None:
        with self.assertRaises(AssertionError):
            self.solution.validIPAddress(None)              # type: ignore
            self.solution.validIPAddress(123)               # type: ignore
            self.solution.validIPAddress(['dasd', 32131])   # type: ignore
            self.solution.validIPAddress({0: 'dsa'})        # type: ignore

if __name__ == '__main__':
    unittest.main()
