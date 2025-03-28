# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy

        while list1 and list2:

            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next
    
# Topics/Data Structures:
#  1. Singly-Linked Lists


# Pitfalls:
#  1. Uhh kinda just familiarizing yourself with linked lists and that a ListNode is literally just a single node and has 2 attributes (val & next)
#  2. Line 20, don't forget to update tail otherwise you're just returning one node. 

# Conceptual Answer:
# Use the common 'dummy' pointer approach. Use a tail variable to point to the next position, depending on if list1 or list2 has the next lower value
# (since we're building the list in ascending order). Once you've reached the end of one list, append the rest of the other list and return dummy.next since
# dummy still remains at the beginning. 
# it'll look like this before returning:
# dummy -> 1 -> 2 -> 3 -> 3 -> 4 -> 6
# by returning dummy.next you return the expected list. 