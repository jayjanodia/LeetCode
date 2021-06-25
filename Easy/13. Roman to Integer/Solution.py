# Reference: https://leetcode.com/problems/roman-to-integer/discuss/6537/My-Straightforward-Python-Solution

#Runtime: 48 ms, faster than 65.86% of Python3 online submissions for Roman to Integer.
#Memory Usage: 14 MB, less than 94.53% of Python3 online submissions for Roman to Integer.

def romanToInt(s):
    '''
    1. Create a dictionary of all the elements in the roman numerals, with the roman numerals being the keys and the numbers being the values.
    2. For each character in the string, if the previous character is of a lower value than the current character, eg. "IV", then subtract the previous character's integer value from the outcome. (so Iteration 1: outcome = 0-1 = -1, Iteration 2: outcome = -1 + 5 = 4)
    3. Else if the previous character is of a higher value than the current character, eg. "VI", then add the characters to the outcome. (Iteration 1: outcome = 0 + 5, Iteration 2: outcome = 5 + 1 = 6)
    4. Final value will be missing since we are just adding the previous character to the output.
    '''
    #1. Create a dictionary of all the elements in the roman numerals, with the roman numerals being the keys and the numbers being the values.
    dictionary = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    #2. For each character in the string, if the previous character is of a lower value than the current character, eg. "IV", then subtract the previous character's integer value from the outcome. (so Iteration 1: outcome = 0-1 = -1, Iteration 2: outcome = -1 + 5 = 4)
    output = 0
    for character in range(1, len(s)):
        if dictionary[s[character-1]] < dictionary[s[character]]:
            output -= dictionary[s[character-1]]
        else:
            output += dictionary[s[character-1]]
    return output + dictionary[s[-1]]

s = 'LVIII'
print(romanToInt(s)) 

# Directly implementable code
class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        output = 0
        for i in range(1, len(s)):
            if dictionary[s[i-1]] < dictionary[s[i]]:
                output -= dictionary[s[i-1]]
            else:
                output += dictionary[s[i-1]]
        return output + dictionary[s[-1]]