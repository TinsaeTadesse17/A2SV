# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 and list2 and list1.val > list2.val:
            temp = list1
            list1 = list2
            list2 = temp

        if not list1:
            return list2
        else:
            dummy = ListNode(0,list1)

        while list1 and list2:
            while list1 and list2 and list1.next and list1.next.val <= list2.val:
                list1 = list1.next
            temp1 = list1.next
            list1.next = list2
            temp2 = list2.next
            list2.next = temp1
            list2 = temp2
            

        if list2:
            list1.next = list2

        return dummy.next

