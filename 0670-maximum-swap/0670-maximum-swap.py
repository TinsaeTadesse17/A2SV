class Solution:
  def maximumSwap(self, num: int) -> int:
    arr = list(str(num))
    
    last = {int(d): i for i, d in enumerate(arr)}
    
    for i, digit in enumerate(arr): # Changed 'num' to 'digit' 
      for d in range(9, int(digit), -1): 
        if last.get(d, -1) > i:
          arr[i], arr[last[d]] = arr[last[d]], arr[i]
          return int(''.join(arr))
    
    return int(num)
