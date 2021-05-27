# Runtime: 64 ms, faster than 62.92% of Python3 online submissions for Longest Substring Without Repeating Characters
# Memory Usage: 14.3 MB, less than 79.33% of Python3 online submissions for Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(s):
    '''
    1. Create a set that will store the characters that have been traversed. The thing about a set is, it doesn't allow duplicate values
    2. Create a sliding window. This is done by creating 2 pointers, a left and a right.
    3. Keep moving right through the string, starting from index 0 of the string. 
    4. If the character at that index is in the set, then remove the character from the set, and move the left pointer ahead by 1, since we now discard the first character in the string and the next character is now the new first character.
    5. If the character at that index is not in the set, then add the character at that index to the set and increment the count by 1. The count is given by r - l
    '''
    # 1. Create a set that will store the characters that have been traversed. The thing about a set is, it doesn't allow duplicate values
    charSet = set()
    # 2. Create a sliding window. This is done by creating 2 pointers, a left and a right.
    l = 0
    r = 0
    #result to store the outcome
    result = 0
    # 3. Keep moving right through the string, starting from index 0 of the string. 
    for r in range(len(s)):
        # 4. If the character at that index is in the string, then clear the set. Set the left pointer at the index the right pointer is currently at
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        # 5. If the character at that index is not in the string, then add the character at that index to the set and increment the count by 1. The count is given by r - l
        charSet.add(s[r])
        result = max(result, r-l+1)
    return result


s = "abcabcbb"
print(lengthOfLongestSubstring(s))




### Directly uploadable solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        result = 0
        for r in range(len(s)):
            print(charSet)
            while s[r] in charSet:
                charSet.remove(s[l])
                print(charSet)
                l += 1
            charSet.add(s[r])
            result = max(result, r-l + 1)
        return result