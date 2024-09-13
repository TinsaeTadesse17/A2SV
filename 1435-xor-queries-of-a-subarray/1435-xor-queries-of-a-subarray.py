class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        prefix_sum = [0]*(len(arr)+1)
        for i in range(len(arr)):
            prefix_sum[i + 1] = prefix_sum[i] ^ arr[i]
        for start,end in queries:
            ans.append(prefix_sum[start] ^ prefix_sum[end + 1])
        return ans


