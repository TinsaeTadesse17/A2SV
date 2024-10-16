class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr = [[a, "a"], [b, "b"], [c, "c"]]
        ans = ""
        
        while True:
            arr.sort(reverse=True)
            
            if arr[0][0] == 0:
                break
            
            if len(ans) >= 2 and ans[-1] == ans[-2] == arr[0][1]:
                if arr[1][0] == 0:
                    break  
                ans += arr[1][1]
                arr[1][0] -= 1
            else:
                ans += arr[0][1]
                arr[0][0] -= 1
        
        return ans
