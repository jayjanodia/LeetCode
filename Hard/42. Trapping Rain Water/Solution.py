# Reference: https://www.youtube.com/watch?v=ZI2z5pq0TqA
# Reference#2: https://www.geeksforgeeks.org/trapping-rain-water/



def brute_force(height):
    '''
    Time Complexity: O(n^2), Space Complexity: O(1)
    THIS CODE WON'T EXECUTE FOR ALL TEST CASES SINCE SOME OF THE TEST CASES ARE EXCEED THE TIME LIMIT
    We must first iterate from the left to the right of the elevation map. For each position, we must see if water poured will overflow. If the water overflows, then continue to the next iteration, otherwise fill that spot with water till it reaches the brim.
    1. Now the elevation map is a list, but for this problem, the elements beyond the list are undefined. The water will overflow if we decide to pour it on the 0th element and the nth element of the list.
       So, we must iterate over the 2nd element till the n-1th element in the list.
    2. Now, we must have 2 pointers, one that will point to the left highest element and another that points to the right highest element. The left highest element will be the left wall while the right highest element will be the right wall to fill in water.
       Basically, we have formed a container that will get filled with water.
    3. The initial iteration is to fill in water such that it does not overflow. To find the walls, we must check the longest wall to the left of the iteration and the longest wall to the right of the iteration. This will give the walls of the container.
    '''
    maximum_water = 0
    # 1. Now the elevation map is a list, but for this problem, the elements beyond the list are undefined. The water will overflow if we decide to pour it on the 0th element and the nth element of the list.
       #So, we must iterate over the 2nd element till the n-1th element in the list.
    for i in range(1,len(height)-1):
        # 2. Now, we must have 2 pointers, one that will point to the left highest element and another that points to the right highest element. The left highest element will be the left wall while the right highest element will be the right wall to fill in water.
        # Basically, we have formed a container that will get filled with water.
        left = height[i]
        right = height[i]
        # 3. The initial iteration is to fill in water such that it does not overflow. To find the walls, we must check the longest wall to the left of the iteration and the longest wall to the right of the iteration. This will give the walls of the container.
        for j in range(0, i):
            left = max(left, height[j]) 
        for j in range(i+1, len(height)):
            right = max(right, height[j])
        maximum_water += min(left, right) - height[i]
    return maximum_water

print('Brute force solution: ')
print(brute_force([0,1,0,2,1,0,1,3,2,1,2,1]))
print(brute_force([4,2,0,3,2,5]))



print('Dynamic Programming Solution')
#Runtime: 52 ms, faster than 80.76% of Python3 online submissions for Trapping Rain Water.
#Memory Usage: 14.9 MB, less than 63.96% of Python3 online submissions for Trapping Rain Water.
def dynamic_programming(height):
    '''
    Time Complexity: O(n), Space Complexity: O(n)
    Instead of finding the left and right pointer at each iteration, iterate through the array calculating the max left and max right at every position.
    1. Initialize 2 arrays, 1 for max left and another for max right. The max left will store the maximum value to the left of it's index from the original array, while the max right will store the maximum value to the right of it's index in the original array.
    2. Iterate through the input list, check if the value of the current index is more than the previously calculated max. If it is, then add the value into the maxLeft list and make it the new previously calculated max. Else if it isn't, then add the previously calculated max to the list.
    3. Reverse the list and perform the same as Step 2 for the maxRight list.
    4. Find the minimum between the each index value from the maxLeft and maxRight lists. Subtract this minimum value by the index value from the height list. This will be the amount of water filled at that particular index. 
    5. Add this amount of water to a variable. The final sum will be the outcome required.
    '''
    #1. Initialize 2 arrays, 1 for max left and another for max right. The max left will store the maximum value to the left of it's index from the original array, while the max right will store the maximum value to the right of it's index in the original array.
    # 2 ways of initializing the array, 1 is by assigning the value 0 to the array and then appending for each new value entered into the array, 2 is by defining the size of the array in the beginning itself, to make it more memory efficient. We'll use option 2
    print(height)
    n = len(height)
    maxLeft = [0] * n
    maxRight = [0] * n
    total_water = 0
    #2. Iterate through the input list, check if the value of the current index is more than the previously calculated max. If it is, then add the value into the maxLeft list and make it the new previously calculated max. Else if it isn't, then add the previously calculated max to the list.
    #1st element of the maxLeft will be the 1st element of the height list
    maxLeft[0] = height[0]
    for i in range(1, n):
        previous_height = height[i]
        previous_maximum = maxLeft[i-1]
        maxLeft[i] = max(previous_maximum, previous_height)
    print(maxLeft)
    #3. Reverse the list and perform the same as Step 2 for the maxRight list.
    #nth element in the maxRight list will be the nth element of the height list
    maxRight[n-1] = height[n-1]
    # Traverse from the second last element to the first element in the height list
    for i in range(n-2, -1, -1):
        previous_height = height[i]
        previous_maximum = maxRight[i+1]
        maxRight[i] = max(previous_height, previous_maximum)
    print(maxRight)
    #4. Find the minimum between the each index value from the maxLeft and maxRight lists. Subtract this minimum value by the index value from the height list. This will be the amount of water filled at that particular index. 
    water_blocks = [0] * n
    for i in range(n):
        water_block = min(maxLeft[i], maxRight[i]) - height[i]
        #5. Add this amount of water to a variable. The final sum will be the outcome required.
        water_blocks[i] = water_block
        total_water += water_block
    print(water_blocks)
    return total_water

print(dynamic_programming([0,1,0,2,1,0,1,3,2,1,2,1]))
#print(dynamic_programming([4,2,0,3,2,5]))


### Directly Implementable Solution
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        height =            [0,1,0,2,1,0,1,3,2,1,2,1]
        maxLeft=            [0,1,1,2,2,2,2,3,3,3,3,3]
        maxRight=           [3,3,3,3,3,3,3,3,2,2,2,1]
        min(left, right)=   [0,1,1,2,2,2,2,3,2,2,2,1]
        min-height=         [0,0,1,0,1,2,1,0,0,1,0,0]
        '''
        # Base case: If list is empty
        if height == []:
            return 0
        
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        final_outcome = 0
        #first value of maxLeft will be the first value in the height list
        maxLeft[0] = height[0]
        #rest of the values of maxLeft will be the maximum between the previous value in maxLeft(the largest value possible in maxLeft) and the current iteration value in the height list
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i-1], height[i])
        
        #traverse the height in the opposite direction to get the values for maxRight
        #last value of maxRight will be the last value in the height list
        maxRight[n-1] = height[n-1]
        #for the rest of the values, they will be filled in the backward direction from the second last element in the height list till the 0th element
        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])
        
        #Find the minimum between each position for maxLeft and maxRight, subtract this minimum by the height at that specific position, add the result to the final_outcome.
        for i in range(n):
            final_outcome += min(maxLeft[i], maxRight[i]) - height[i]
        return final_outcome



# Final Solution: Time Complexity: O(n), Space Complexity: O(1)
#Runtime: 52 ms, faster than 80.77% of Python3 online submissions for Trapping Rain Water.
#Memory Usage: 14.8 MB, less than 85.53% of Python3 online submissions for Trapping Rain Water.

def dynamic_programming_optimized(height):
    '''
    1. Create 2 pointers, left and right. Left pointer points to the first element in the array, Right pointer points to the last element in the array.
    2. Find the smaller value between the 2 pointers and shift the pointer with the smaller value
    3. Find the difference between the original value and the new shifted value from step 2. If the difference is less than 0, that is, the new shifted value is larger than the previous value, then just change the pointer's value to the shifted value.
    4. Else if the difference is greater than 0, that is, the new shifted value from step 2 is less than the original value, then add that value to the final outcome and change the pointer's value to the shifted value. Continue till the left and right pointers don't meet.
    '''
    # Base case if list is empty
    if height == []:
        return 0
        
    left_max = 0
    right_max = 0
    final_outcome = 0
    n = len(height)
    # 1. Create 2 pointers, left and right. Left pointer points to the first element in the array, Right pointer points to the last element in the array.
    left = 0
    right = n-1
    while left < right:
        # 2. Find the smaller value between the 2 pointers and shift the pointer with the smaller value
        if height[left] < height[right]:
            # 3. Find the difference between the original value and the new shifted value from step 2. If the difference is less than 0, that is, the new shifted value is larger than the previous value, then just change the pointer's value to the shifted value.
            if left_max - height[left] < 0:
                left_max = height[left]
            else:
                # 4. Else if the difference is greater than 0, that is, the new shifted value from step 2 is less than the original value, then add that value to the final outcome, subtract this value by the current value in the original array, and increment the pointer. Continue till the left and right pointers don't meet.
                final_outcome += left_max - height[left]
            left += 1
        elif height[right] <= height[left]:
            if right_max - height[right] < 0:
                right_max = height[right]
            else:
                final_outcome += right_max - height[right]
            right -= 1

    return final_outcome

print(dynamic_programming_optimized([0,1,0,2,1,0,1,3,2,1,2,1]))

### Directly implementable solution
class Solution:
    def trap(self, height: List[int]) -> int:
        #Base case
        if height == []:
            return 0
        
        n = len(height)
        left = 0
        right = n-1
        final_outcome = 0
        leftMax, rightMax = height[left], height[right]
        
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                final_outcome += leftMax - height[left]
                
            elif leftMax >= rightMax:
                val = height[right]
                right -= 1
                rightMax = max(rightMax, height[right])
                final_outcome += rightMax - height[right]
                
        return final_outcome