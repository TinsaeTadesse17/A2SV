# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        dummy.next = head
        while head and head.next:
            new_node = ListNode(math.gcd(head.val,head.next.val))
            new_node.next = head.next
            head.next = new_node
            head = head.next.next
        return dummy.next

        



        