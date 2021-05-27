# Runtime: 60 ms, faster than 19.99% of Python3 online submissions for Two Sum.
# Memory Usage: 15.3 MB, less than 9.73% of Python3 online submissions for Two Sum.

def brute_force(nums, target):
    '''Brute Force Approach
    Time Complexity: O(n^2)
    1. Start from the first element in the list
    2. Compare it with each element after it
    3. If the addition of the first element and any other element is equal to the target then return the indices of the first element and the other element
    4. If the addition is not equal then compare the second element in the list with each other element after it. '''
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

def twoSum(nums, target):
    ''' Note that the output should be the index of the numbers in the list, not the numbers itself, so you'll get a wrong outcome if you decide to sort the list
    1. Create an empty dictionary
    2. Start with the first element in the list. Subtract the target with this element.
    3. Find the subtracted value from the hashmap/dictionary. 
    4. If the value does not exist, then add the element to the dictionary as the key along with it's index as the value'''
    # 1. Create an empty dictionary
    dictionary = {}
    # 2. Start with the first element in the list. Subtract the target with this element.
    for i in range(len(nums)): # can also use: for i, n in enumerate(nums): 
        sub = target - nums[i]
        # 3. Find the subtracted value from the hashmap/dictionary.
        if sub in dictionary:
            return [dictionary[sub], i]
        # If the value does not exist, then add the element to the dictionary as the key along with it's index as the value
        dictionary[nums[i]] = i

nums = [3,3]
target = 6
print(brute_force(nums, target))


### Solution for direct submission
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' Note that the output should be the index of the numbers in the list, not the numbers itself, so you'll get a wrong outcome if you decide to sort the list
    1. Create an empty dictionary
    2. Start with the first element in the list. Subtract the target with this element.
    3. Find the subtracted value from the hashmap/dictionary. 
    4. If the value does not exist, then add the element to the dictionary as the key along with it's index as the value'''
        # 1. Create an empty dictionary
        dictionary = {}
        # 2. Start with the first element in the list. Subtract the target with this element.
        for i, n in enumerate(nums):
            sub = target - n
            # 3. Find the subtracted value from the hashmap/dictionary.
            if sub in dictionary:
                return [dictionary[sub], i]
            # If the value does not exist, then add the element to the dictionary as the key along with it's index as the value
            dictionary[n] = i
        return