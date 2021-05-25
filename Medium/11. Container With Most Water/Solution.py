# Runtime: 632 ms, faster than 95.24% of Python3 online submissions for Container With Most Water.
# Memory Usage: 26.1 MB, less than 97.82% of Python3 online submissions for Container With Most Water.

def maxArea(height):
    '''
    As we can see in the diagram, we must find the area of a rectangle.
    We know that the area of a rectangle is given as width * height. 
    We need to find the maximum area available
    1. For each line find the width. This is given as, initially the length of the list given - 1, that will decrease for each iteration we do in the list
    2. The height will be the minimum of 2 lines. Let's create 2 pointers, one for the left line and one for the right.
    3. If the left pointer has a lower value than the right pointer, then the left pointer will be the height and vice versa.
    4. If the left pointer had the lower value, then increment the left pointer. If the right pointer had the lower value, decrement the right pointer.
    5. Calculate the area based on the height found and the width.
    6. Compare the area with the maxArea. If the area is greater, then maxArea = area.
    7. When you reach the end of the list, return the maxArea. That's what we want
    '''
    # Find the length of the array given
    length = len(height)
    w = length
    # Left pointer points to the leftmost element in the array
    l = 0
    # Right pointer points to the rightmost element in the array
    r = length-1
    # Initialize the max_area
    max_area = -1
    # We must ensure that the left and right pointer donot cross, otherwise we will have an infinite loop
    while l != r:
        # If the left pointer has a lower value than the right pointer, then the left pointer will be the height
        if height[l] < height[r]:
            h = height[l]
            w = w - 1
            # Width decrements by 1 since we have moved ahead in the container
            area = w * h
            l += 1
        else:
            h = height[r]
            w = w - 1
            area = w * h
            r -= 1
        if max_area < area:
            max_area = area
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))



### Directly Uploadable Solution

class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        w = length
        l = 0
        r = length-1
        max_area = -1
        while l != r:
            if height[l] < height[r]:
                h = height[l]
                w = w - 1
                area = w * h
                l += 1
            else:
                h = height[r]
                w = w - 1
                area = w * h
                r -= 1
            if max_area < area:
                max_area = area
        return max_area