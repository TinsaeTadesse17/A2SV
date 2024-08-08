# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit = head
        tortoise = head

        while rabbit and tortoise and rabbit.next and tortoise.next:
            
            rabbit = rabbit.next.next
            tortoise = tortoise.next
            if rabbit == tortoise:
                return True

        return False