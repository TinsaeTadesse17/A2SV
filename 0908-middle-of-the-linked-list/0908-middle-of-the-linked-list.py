# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        rabbit , turtle = dummy , dummy

        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            turtle = turtle.next
        while rabbit:
            rabbit = rabbit.next
            turtle = turtle.next
            
        return turtle