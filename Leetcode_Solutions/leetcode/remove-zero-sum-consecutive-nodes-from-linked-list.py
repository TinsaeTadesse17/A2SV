# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        node_map = {0: dummy}
        prefix_sum = 0
        
        while head:
            prefix_sum += head.val
            if prefix_sum in node_map:
                to_remove = node_map[prefix_sum].next
                tmp_sum = prefix_sum + to_remove.val
                while tmp_sum != prefix_sum:
                    del node_map[tmp_sum]
                    to_remove = to_remove.next
                    tmp_sum += to_remove.val
                node_map[prefix_sum].next = head.next
            else:
                node_map[prefix_sum] = head
            head = head.next
        
        return dummy.next
