class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        
        curr = head
        while curr:
            array.append(curr.val)
            curr = curr.next

        size = len(array)
        for i in range(1, size):
            j = i - 1
            while j >= 0 and array[j] > array[j + 1]: 
                array[j + 1], array[j] = array[j], array[j + 1]
                j -= 1

        # Reconstruct the sorted linked list
        sorted_head = ListNode(array[0])
        curr = sorted_head
        for i in range(1, size):
            curr.next = ListNode(array[i])
            curr = curr.next

        return sorted_head
