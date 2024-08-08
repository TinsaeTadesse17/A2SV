class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

      from collections import defaultdict
      count = 0

      mydict = defaultdict(int)
      
      for j in ranges:

        for k in range(j[0],j[1]+1):
          mydict[k] = k
        
      for i in range(left,right+1):
        
        if i in mydict:
          count +=1

      return count == right-left + 1
        
            