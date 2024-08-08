class Solution:
  def isPalindrome(self, x: int) -> bool:

    backward = ""
    num = str(x)
    for i in range(len(num)-1,-1,-1):
        backward+=num[i]
    return backward == num
        
