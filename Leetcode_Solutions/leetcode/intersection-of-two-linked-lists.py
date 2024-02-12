# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        length_a = 0
        length_b = 0

        p1 = headA
        p2 = headB


        while p1:
            length_a += 1
            p1 = p1.next

        while p2:
            length_b += 1
            p2 = p2.next

        p1 = headA
        p2 = headB

        if length_a > length_b:
            for _ in range(abs(length_a-length_b)):
                p1 = p1.next
        else:
            for _ in range(abs(length_a-length_b)):
                p2 = p2.next

        while p1 and p2:

            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next

        return None
            


        




        

