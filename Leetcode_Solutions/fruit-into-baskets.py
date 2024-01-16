class Solution:
  def totalFruit(self, fruits: List[int]) -> int:
    ans = 0
    count = defaultdict(int)

    left = 0
    
    for right, fruit in enumerate(fruits):
        count[fruit] += 1

        while len(count) > 2:
            count[fruits[left]] -= 1

            if count[fruits[left]] == 0:
                del count[fruits[left]]
            
            left += 1

        ans = max(ans, right - left + 1)

    return ans