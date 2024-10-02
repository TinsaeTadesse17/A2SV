class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans = []
        hashmap = {}
        array = sorted(set(arr))

        for idx,num in enumerate(array):
            hashmap[num] = idx+1

        for num in arr:
            ans.append(hashmap[num])
        
        return ans