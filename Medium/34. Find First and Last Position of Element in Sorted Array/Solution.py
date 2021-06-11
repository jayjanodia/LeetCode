#Runtime: 84 ms, faster than 71.32% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
#Memory Usage: 15.2 MB, less than 95.41% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

def searchRange(nums, target):
    '''
    1. Create 2 pointers, the left pointer and the right pointer. The left pointer points to the left-most element in the list while the right pointer points to the right-most element.
    2. If the target is not in the list, then return [-1, -1] as expected.
    3. Now compare the left and right pointer values. If both have the same values, then return the index of the left and right pointers. Else, if the value of the left pointer is less than the target, then increment the left pointer index. Also, if the value of the right pointer is greater than the target, then decrement the right pointer index.
    Note that this method only works since the list is sorted.
    '''



#Directly implementable solution
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 1. Create 2 pointers, the left pointer and the right pointer. The left pointer points to the left-most element in the list while the right pointer points to the right-most element.
        l = 0
        r = len(nums) - 1
        
        #2. If the target is not in the list, then return [-1, -1] as expected.
        if target not in nums:
            return [-1, -1]
        
        while nums[l] != nums[r]:
            if nums[l] < target:
                l += 1
            elif nums[r] > target:
                r -= 1
                
        return [l, r]