class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverseStr(s: List[str],i,j):

            if  j <= i:
                return s
            
            s[i] , s[j] = s[j] , s[i]
            i += 1
            j -= 1 
            return reverseStr(s,i,j)  
            

        return reverseStr(s,0,len(s)-1)

        
             