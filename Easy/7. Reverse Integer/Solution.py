# Runtime: 32 ms, faster than 65.49% of Python3 online submissions for Reverse Integer.
# Memory Usage: 14 MB, less than 98.08% of Python3 online submissions for Reverse Integer.

def reverse(x):
    '''
    1. Create a variable to store the reverse of the given number
    2. Check if the number is positive or negative. If the number is positive, no problem. If the number is negative, then convert the number to positive and take it's sign out.
    3. Now we will keep dividing the number by 10 while multiplying the reverse number by 10 while keeping it's remainder, while the number is greater than 0.
    4. If the output number is less than -2^31 or greater than 2^31-1, return 0.
    '''
    #1. Create a variable to store the reverse of the given number
    num_reverse = 0
    #2. Check if the number is positive or negative. If the number is positive, no problem. If the number is negative, then convert the number to positive and take it's sign out.
    sign = 0
    if x > 0:
        sign = 1
    else:
        sign = -1
        x = abs(x)
    #3. Now we will keep dividing the number by 10 while multiplying the reverse number by 10 while keeping it's remainder, while the number is greater than 0.
    while x > 0:
        remainder = x % 10
        num_reverse = (num_reverse*10) + remainder
        x = x // 10
    #4. If the output number is less than -2^31 or greater than 2^31-1, return 0.
    if num_reverse < (-2**31) or num_reverse > (2**31 - 1):
        return 0
    return num_reverse * sign


### Solution for direct submission
class Solution:
    def reverse(self, x: int) -> int:
        num_reverse = 0
        sign = 0
        if x > 0:
            sign = 1
        else:
            sign = -1
            x = abs(x)
        while x > 0:
            remainder = x % 10
            num_reverse = (num_reverse*10) + remainder
            x = x // 10
        if num_reverse < (-2**31) or num_reverse > (2**31 - 1):
            return 0
        return num_reverse * sign
            