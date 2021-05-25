# Runtime: 88 ms, faster than 81.85% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 14.3 MB, less than 92.71% of Python3 online submissions for Median of Two Sorted Arrays.

def brute_force(nums1, nums2):
    '''
    Given: The arrays are sorted
    1. Merge/concatenate the 2 arrays and sort the new array
    2. If the new array has an odd length, then there is just 1 median, which will be length//2
    3. If the new array has an even length, then there are 2 medians, which will be length//2 - 1 and length//2. Find the avg.
    '''
    # Concatenate the 2 arrays. Time Complexity: O(1)
    nums3 = nums1 + nums2
    # Sort the new array. Time Complexity: O(n log n)
    nums3.sort()
    length = len(nums3)
    # If the new array has an odd length, then there is just 1 median. Time Complexity: O(1)
    if length % 2 == 1:
        median = nums3[length//2]
    # If the new array has an even length, then there are 2 medians. Time complexity: O(1)
    else:
        median = (nums3[length//2 - 1] + nums3[length//2])/2
    return median

    # Total Time Complexity: O(n log n)
    


### Directly Uploadable Solution
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Concatenate the 2 arrays. Time Complexity: O(1)
        nums3 = nums1 + nums2
        # Sort the new array. Time Complexity: O(n log n)
        nums3.sort()
        length = len(nums3)
        # If the new array has an odd length, then there is just 1 median
        if length % 2 == 1:
            median = nums3[length//2]
        # If the new array has an even length, then there are 2 medians
        else:
            median = (nums3[length//2 - 1] + nums3[length//2])/2
        return median

