# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        self.left = left
        self.right = right
        self.head = head
        ptr1 = head
        ptr2 = head
        ptr3 = head
        ptr4 = head

        for i in range(right):
            if not head:
                return
            elif i == left-2:
                ptr1 = head
                ptr2 = head.next
                head.next = None
                head = ptr2
                continue
            elif i == right-1:
                ptr3 = head
                ptr4 = head.next
                head.next = None
            head = head.next

        curr = ptr2
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        ptr2.next = ptr4

        if ptr1 != ptr2:
            ptr1.next = ptr3
        else:
            return ptr3
        
        
        return self.head


        

        
