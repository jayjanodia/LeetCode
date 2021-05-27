# Runtime: 1220 ms, faster than 50.44% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14.2 MB, less than 81.75% of Python3 online submissions for Longest Palindromic Substring.

def is_palindrome(l, r, s):
    result = ''
    result_length = 0
    # Ensure that the left and right pointers never pass the range of the string
    # 2. Check whether the character to it's left matches the character to it's right. If it doesn't move on to the next character.
    # 3. If the character to it's left matches with the character to it's right, then view the next left and right elements.    
    while l >=0 and r < len(s) and s[l] == s[r]:
        # If the length of the palindrome is greater than the length of the result of the previously long palindrome, then the previously long palindrome will now become the new palindrome 
        if (r - l + 1) > result_length:
            result = s[l:r+1]
            result_length = len(result) # or (r-l+1)
        l -= 1
        r += 1
    return result

def longestPalindrome(s):
    '''
    1. Start from the first character in the string. This will act as the middle of our palindromic substring
    2. Check whether the character to it's left matches the character to it's right. If it doesn't move on to the next character.
    3. If the character to it's left matches with the character to it's right, then view the next left and right elements.
    '''
    # 1. Start from the first character in the string. This will act as the middle of our palindromic substring
    for i in range(len(s)):
        # Initialize the left and right pointer. The left pointer will move left and the right pointer will move right
        l = i
        r = i
        # Will work for odd length palindromes
        res = is_palindrome(l, r, s)
        # Will work for even length palindromes
        l = i
        r = i + 1
        res = is_palindrome(l, r, s)
    return res


### Directly impementable solution
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