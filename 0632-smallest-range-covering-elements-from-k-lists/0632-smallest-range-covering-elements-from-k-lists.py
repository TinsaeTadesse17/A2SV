class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Min-heap to store (value, list_index, element_index) tuples
        min_heap = []
        curr_max = float('-inf')  # max element across all lists
        
        #  first element of each list is put in heap
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            curr_max = max(curr_max, nums[i][0])
        
        min_range = [float('-inf'), float('inf')]
        
        while min_heap:
            curr_min, list_idx, elem_idx = heapq.heappop(min_heap)
            
            if curr_max - curr_min < min_range[1] - min_range[0]:
                min_range = [curr_min, curr_max]
            
            # end of one of the lists then break
            if elem_idx + 1 == len(nums[list_idx]):
                break
            
            # Push the next element from the same list into heap
            nxt = nums[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (nxt, list_idx, elem_idx + 1))
            
            curr_max = max(curr_max, nxt)
        
        return min_range
