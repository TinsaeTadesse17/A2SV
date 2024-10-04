# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0,head)
        rabbit , tortoise = dummy , dummy

        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            tortoise = tortoise.next
        while rabbit:
            rabbit = rabbit.next
            tortoise = tortoise.next

        prev = None
        while tortoise:
            temp = tortoise.next
            tortoise.next = prev
            prev = tortoise
            tortoise = temp

        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True




