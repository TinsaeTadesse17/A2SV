class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        hashmap = defaultdict(int)
        ans = []
        idx = -1

        for i,char in enumerate(s):
            hashmap[char] += 1
            if hashmap[char] == counter[char]:
                del hashmap[char]
            if not hashmap:
                ans.append(i-idx)
                idx = i

        return ans
            

