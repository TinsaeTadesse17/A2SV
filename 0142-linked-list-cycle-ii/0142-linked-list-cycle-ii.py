# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rabbit , tortoise = head , head

        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            tortoise = tortoise.next

            if rabbit == tortoise:
                tortoise = head
                while rabbit != tortoise:
                    tortoise = tortoise.next
                    rabbit = rabbit.next
                return tortoise

        return None


