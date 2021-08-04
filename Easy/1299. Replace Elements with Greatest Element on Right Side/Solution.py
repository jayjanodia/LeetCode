# Runtime: 120 ms, faster than 82.05% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
# Memory Usage: 15.7 MB, less than 15.06% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
def my_solution(arr):
    '''
    Time Complexity: O(n), Space Complexity: O(n)
    1. Create an output array of the same length as the given input array.
    2. The last element in the array will be -1
    3. Traverse the input array in a reverse order. Find the maximum between the immediate right of the input array's and the immediate right of the output array's current iteration, and store the outcome in the output array's current iteration.
    '''
    n = len(arr)
    # 1. Create an output array of the same length as the given input array.
    outcome = [0] * n
    # 2. The last element in the array will be -1
    outcome[n-1] = -1
    #3. Traverse the input array in a reverse order. Find the maximum between the immediate right of the input array's and the immediate right of the output array's current iteration, and store the outcome in the output array's current iteration.
    for i in range(n-2, -1, -1):
        outcome[i] = max(arr[i+1], outcome[i+1])
    return outcome


# Directly implementable solution
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        # 1. Create an output array of the same length as the given input array.
        outcome = [0] * n
        # 2. The last element in the array will be -1
        outcome[n-1] = -1
        #3. Traverse the input array in a reverse order. Find the maximum between the immediate right of the input array's and the immediate right of the output array's current iteration, and store the outcome in the output array's current iteration.
        for i in range(n-2, -1, -1):
            outcome[i] = max(arr[i+1], outcome[i+1])
        return outcome


# Runtime: 120 ms, faster than 82.05% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
# Memory Usage: 15.2 MB, less than 96.45% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
# Reference: https://www.youtube.com/watch?v=ZHjKhUjcsaU
def better_solution(arr):
    '''
    Time Complexity: O(n), Space Complexity: O(1)
    1. Initiate the maximum value of the new array to be -1.
    2. Traverse the initial array in the reverse order
    3. Find the maximum between the initiated maximum value and the current element in the array
    4. Store the initiated maximum value in the current element in the array and the maximum found as the new maximum value.
    '''
    # 1. Initiate the maximum value of the new array to be -1.
    maximum = -1
    # 2. Traverse the initial array in the reverse order
    for i in range(len(arr)-1, -1, -1):
        # 3. Find the maximum between the initiated maximum value and the current element in the array
        new_max = max(maximum, arr[i])
        arr[i] = maximum
        maximum = new_max
    return arr