class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    '''
    1. Initialize the current node to a dummy head of the returning list
    2. Initialize the carry to 0
    3. Initialize p and q as the head of l1 and l2 respectively
    4. Loop through lists l1 and l2 until you reach both ends
    5. Set x to node p's value. If p has reached the end of l1, set to 0
    6. Set y to node q's value. If q has reached the end of l2, set to 0
    7. Set sum = x + y + carry
    8. Update carry = sum/10
    9. Create a new node with the digit value of sum % 10 and set it to the current node's next, then advance current node to next
    10. Advance both p and q
    11. Check if carry = 1, if so append a new node with digit 1 to the returning list.
    12. Return dummy head's next node.
    '''
    # Initialize the current node to a dummy head of the returning list
    dummy = ListNode()
    currnode = dummy
    # Initialize the carry to 0
    carry = 0
    # while l1 or l2 are not at the end / while l1 and l2 are not null
    # Handling the edge case: If in the end a carry is remaining but l1 or l2 are null, the loop will exit. We don't want that.
    # So what we do is even if l1 or l2 are null, if a carry exists, then x = 0 and y = 0, but carry will be 1, so the final
    # outcome will be 1.
    while l1 or l2 or carry:
        #set x to l1's value. If l1 has reached it's end, then set x to 0
        if l1:
            x = l1.val
        else:
            x = 0
        #set y to l2's value. If l2 has reached it's end, then set y to 0
        if l2:
            y = l2.val
        else:
            y = 0
        # set sum = x + y + carry
        sum = x + y + carry
        # update carry = int(sum / 10)
        carry = sum // 10
        # set sum = sum % 10
        sum = sum % 10
        # Create a new node and set it to the current node's next
        currnode.next = ListNode(sum)
        # Advance current node to next node
        currnode = currnode.next
        #Advance both l1 and l2 
        if l1:
            l1 = l1.next
        else:
            l1 = None
        if l2:
            l2 = l2.next
        else:
            l2 = None

    return dummy.next 

#l1 = [2, 4, 3]
l1 = ListNode()
l1.val = 2
l1.next = ListNode()
l1.next.val = 4
l1.next.next = ListNode()
l1.next.next.val = 3
#l2 = [5, 6, 4]
l2 = ListNode()
l2.val = 5
l2.next = ListNode()
l2.next.val = 6
l2.next.next = ListNode()
l2.next.next.val = 4

l3 = addTwoNumbers(l1, l2)
list_l3 = []
while l3:
    list_l3.append(l3.val)
    l3 = l3.next

print(list_l3)

### Directly uploadable solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize a dummy node
        dummy = ListNode()
        # Set the current node to the dummy node (here, the curnode will initially be the head)
        currNode = dummy
        # Set carry = 0
        carry = 0
        
        #while l1 != null or l2 != null or carry != 0
        while l1 or l2 or carry:
            # set the value of x to the node l1's value. If l1 is null, then set x to 0
            x = l1.val if l1 else 0
            # set the value of y to the node l2's value. If l2 is null, then set y to 0
            y = l2.val if l2 else 0
            #add the value of x + y + carry to the sum
            sum = x + y + carry
            # check if carry is generated or not
            carry = sum // 10
            # ensure that the sum only has the unit's digit place
            sum %= 10
            # Create a new node and set it to the current node's next
            currNode.next = ListNode(sum)
            #Advance curNode to the next node
            currNode = currNode.next
            # Advance both l1 and l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
        