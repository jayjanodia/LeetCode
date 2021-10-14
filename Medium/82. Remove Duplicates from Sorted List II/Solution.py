class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head):
        # Node to handle the case in case we just have one root node and the elements after that are all the same as the root node
        sentinel = Node(0, head)

        # Predecessor node that will always be a distinct value
        pred = sentinel

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            
            else:
                pred = pred.next
            head = head.next
        return sentinel.next


# Directly Implementable Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Creating a sentinel node
        # This node is for handling the case where we just have the same number in the linked list
        # eg 9-->9-->9-->null
        sentinel = ListNode(0, head)
        
        # Create a predecessor node that will act as the last node before the sublist of duplicates
        # comes in
        pred = sentinel
        
        while head:
            # if the current node value and the next node value are the same, then while the current
            #value and the next value are the same, keep going to the next node
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                # Point the predecessor node to the next node, so now the predecessor node is linked to a new node value
                pred.next = head.next
            # Else if the current node value and the next node value are not the same then go to the next value in the linked list.
            else:
                pred = pred.next
            head = head.next
        return sentinel.next