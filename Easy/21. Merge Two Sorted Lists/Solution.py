#Runtime: 32 ms, faster than 92.73% of Python3 online submissions for Merge Two Sorted Lists.
#Memory Usage: 14.3 MB, less than 30.89% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        1. Create a dummy node to store the result in
        2. Compare the value of each list and see which value is less. Add that value to the dummy list.
        3. Check if either one of the lists still has elements in them. If they do, add that list to the remainder of the dummy'''
        # Create a dummy node
        output = dummy = ListNode()
        
        # Compare the value of each list and see which value is less. Add that value to the dummy list
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            elif l2.val <= l1.val:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        # Check if either one of the lists still have elements in them. If they do, add that list to the remainder of the dummy
        if l1:
            dummy.next = l1
        elif l2:
            dummy.next = l2
        return output.next