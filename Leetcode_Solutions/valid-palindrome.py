class Solution:
    def isPalindrome(self, s: str) -> bool:
        b=s.lower()
        l=0
        r=len(b)-1
        while l<r:
            if not b[l].isalnum():
                l+=1
            if not b[r].isalnum():
                r-=1
            if b[r].isalnum() and b[l].isalnum():
                if b[l]!=b[r]:
                    return False
                r -=1
                l+=1
        return True
        