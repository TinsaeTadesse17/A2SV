class Solution:
    def getRow(self, n: int) -> List[int]:
        p_triangle = {0: [1]}
        
        if n in p_triangle:
            return p_triangle[n]
        
        p_triangle[n] = self.rowPascal(self.getRow(n-1))
    
        return p_triangle[n]
    
    def rowPascal(self, arr):
        ans = []
        ans.append(1)
        for i in range(len(arr)-1):
            x =  arr[i] + arr[i+1]
            ans.append(x)
        ans.append(1)
        return ans