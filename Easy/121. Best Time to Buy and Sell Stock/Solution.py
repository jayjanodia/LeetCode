#Runtime: 988 ms, faster than 80.13% of Python3 online submissions for Best Time to Buy and Sell Stock.
#Memory Usage: 25 MB, less than 81.80% of Python3 online submissions for Best Time to Buy and Sell Stock.

class Solution:
    '''
    1. Traverse through the initial list and at each co-ordinate check if the value is the minimum value.
    2. Find the maximum difference between the previous maximum value and the new difference between the price value of the item and the minimum value.'''
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf')
        maximum = 0
        for i in range(len(prices)):
            if minimum > prices[i]:
                minimum = prices[i]
            maximum = max(maximum, prices[i]-minimum)
        return maximum

    