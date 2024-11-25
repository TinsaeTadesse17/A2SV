class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        def recursive_function(left,right,s):
            if left >= right:
                return s
            s[left] , s[right] = s[right] , s[left]
            return recursive_function(left+1,right-1,s)
        return recursive_function(0,n-1,s)

        