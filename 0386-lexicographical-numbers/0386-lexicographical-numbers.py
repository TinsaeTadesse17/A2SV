class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [i for i in range(1,n+1)]
        ans = list(map(str,ans))

        ans.sort()
        ans = list(map(int,ans))
        
        return ans
