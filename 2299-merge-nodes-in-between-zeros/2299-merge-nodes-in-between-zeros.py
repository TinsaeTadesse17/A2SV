# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        new_head = dummy
        head = head.next
        curr_sum = 0

        while head:
            if head.val != 0:
                curr_sum += head.val
            else:
                new_node = ListNode(curr_sum)
                new_head.next = new_node
                new_head = new_head.next
                curr_sum = 0
            head = head.next

        return dummy.next
