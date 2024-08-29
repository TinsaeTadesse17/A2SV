# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = [i for i in range(n)]
        ranks = [0] * n
        count = 0

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            if ranks[rootX] > ranks[rootY]:
                parent[rootY] = rootX
                ranks[rootX] += ranks[rootY]
            else:
                parent[rootX] = rootY
                ranks[rootY] += ranks[rootX]
            return True

        
        for i in range(len(stones)):
            for j in range(i,len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    if union(i,j):
                        count += 1


        return count