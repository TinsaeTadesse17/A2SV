# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        
        def mergeLists(list1,list2,current):
            
            if not list1 or not list2:
                if list1:
                    current.next = list1
                elif list2:
                    current.next = list2
                return dummy.next
            
            elif list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
                return mergeLists(list1,list2,current)
                
            elif list1.val > list2.val:
                current.next = list2
                list2 = list2.next
                current = current.next
                return mergeLists(list1,list2,current)
            
            


        return mergeLists(list1,list2,current)

    
