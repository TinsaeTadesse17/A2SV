class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        mydict = defaultdict(list)
        
        res = []
        ans = []

        for i in range(len(mat)):

            for j in range(len(mat[0])):

                mydict[i+j].append(mat[i][j])

        
        for k in mydict.keys():

            if k % 2 == 0:
                res.append((mydict[k])[::-1])
                
            else:
                res.append(mydict[k])

        ans = [item for subarray in res for item in subarray]
        return ans
        
        