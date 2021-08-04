#Runtime: 40 ms, faster than 52.14% of Python3 online submissions for Beautiful Array.
#Memory Usage: 14.1 MB, less than 97.14% of Python3 online submissions for Beautiful Array.

class Solution:
    def beautifulArray(n):
        '''
        Step 1: Initialize an array with 1 arr = [1]
        Step 2: While the length of the array is less than n, create 2 arrays, one for storing odd numbers and the other for storing even numbers
        Step 3: For each element in the array, add the element*2 - 1 in the odd array, and element*2 in the even array. Ensure that each value added in the array is less than n
        Step 4: Concatenate the two arrays'''
        # Step 1: Initialize an array with 1 arr = [1]
        arr = [1]

        #Step 2: While the length of the array is less than n, create 2 arrays, one for storing odd numbers and the other for storing even numbers
        while len(arr) < n:
            odd_arr = []
            even_arr = []
            # Step 3: For each element in the array, add the element*2 - 1 in the odd array, and element*2 in the even array. Ensure that each value added in the array is less than n
            for i in arr:
                if 2*i-1 <= n:
                    odd_arr.append(2*i-1)
                if 2*i <= n:
                    even_arr.append(2*i)
                # Step 4: Concatenate the two arrays
                arr = odd_arr + even_arr

    