class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Reverse the first half of the linked list while finding the middle
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse the first half of the linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # Compare the reversed first half with the second half
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        
        return True
