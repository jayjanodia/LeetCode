#Runtime: 360 ms, faster than 70.67% of Python3 online submissions for Find All Duplicates in an Array.
#Memory Usage: 21.7 MB, less than 84.86% of Python3 online submissions for Find All Duplicates in an Array.

def findDuplicates(nums):
    '''
    We are given that all the numbers are positive. So, one logic is to go through the elements and check if that location has a negative value.
    If it does have a negative value that means we have already got that number. So that number is a duplicate number.'''

    # List of duplicate numbers
    duplicates =[]
    for i in nums:
        if nums[abs(i)-1] < 0:
            duplicates.append(abs(i))
        else:
            nums[abs(i)-1] *= -1
    return duplicates