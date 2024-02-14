# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode()  # Dummy node 
        less_tail = less_head   # Dummy node
        greater_head = ListNode()  # Dummy node 
        greater_tail = greater_head   # Dummy node
        
        curr = head
        while curr:
            if curr.val < x:
                less_tail.next = curr
                less_tail = less_tail.next
            else:
                greater_tail.next = curr
                greater_tail = greater_tail.next
            curr = curr.next
        
        # Connect the tail of the less-than partition to the head of the greater-than-or-equal-to partition
        greater_tail.next = None
        less_tail.next = greater_head.next
        
        return less_head.next




        

        