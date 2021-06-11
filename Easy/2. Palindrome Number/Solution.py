# Runtime: 56 ms, faster than 75.41% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14.4 MB, less than 13.65% of Python3 online submissions for Palindrome Number.

def reverse_number(x):
    '''
    simply reverse x and see if the the reversed value of x and original x match
    '''
    x_orig = x
    x_rev = 0
    while x_orig > 0:
        remainder = x_orig % 10
        x_rev = (x_rev * 10) + remainder
        x_orig = x_orig // 10
    if x == x_rev:
        return True
    else:
        return False

### Solution for direct submission
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        result_length = 0
        for i in range(len(s)):
            #for odd length string
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > result_length:
                    result = s[l:r+1]
                    result_length = r - l + 1
                l -= 1
                r += 1
            #for even length string
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > result_length:
                    result = s[l:r+1]
                    result_length = r - l + 1
                l -= 1
                r += 1
        return result