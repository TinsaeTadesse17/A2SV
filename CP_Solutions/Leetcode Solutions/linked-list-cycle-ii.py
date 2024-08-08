# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rabbit = head
        tortoise = head

        while rabbit and tortoise and rabbit.next and tortoise.next:
            
            rabbit = rabbit.next.next
            tortoise = tortoise.next
            if rabbit == tortoise:
                rabbit = head
                while rabbit != tortoise:
                    rabbit=rabbit.next
                    tortoise=tortoise.next
                return rabbit
                
        return None

        