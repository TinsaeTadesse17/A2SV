class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n

       
        count, moves = 0, 0
        for i in range(n):
            ans[i] += moves
            count += 1 if boxes[i] == '1' else 0
            moves += count

     
        count, moves = 0, 0
        for i in range(n - 1, -1, -1):
            ans[i] += moves
            count += 1 if boxes[i] == '1' else 0
            moves += count

        return ans