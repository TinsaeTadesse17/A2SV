class Solution:
    def totalMoney(self, n: int) -> int:
      arr = [1,2,3,4,5,6,7]
      money = 0

      for i in range(n):
        money += arr[i%7]
        arr[i%7] += 1

      return money

        
            
            
            