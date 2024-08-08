class Solution:
    def sortSentence(self, s: str) -> str:

        arr = s.split()
        ans = [0] * len(arr)

        for i in range(len(arr)):
            ans[int(arr[i][-1])-1] = arr[i][:len(arr[i])-1]

        return ' '.join(ans)
        

