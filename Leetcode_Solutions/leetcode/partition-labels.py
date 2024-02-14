class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = 0
        ans = []
        curr = set()
        counter = Counter(s)
        for i in range(len(s)):
            end = i+1
            counter[s[i]] -= 1
            curr.add(s[i])

            for val in curr:
                if counter[val] != 0:
                    break
            else:
                ans.append(end-start)
                start = end

        return ans


