class Solution:
    def countUnguarded(self, m, n, guards, walls):
        visited = [[False] * n for _ in range(m)]
        st, st1 = set(), set()
        guarded = 0
        
        for i in range(len(walls)):
            st.add((walls[i][0], walls[i][1]))
        
        for i in range(len(guards)):
            st1.add((guards[i][0], guards[i][1]))
        
        for i in range(len(guards)):
            l, r, u, d = guards[i][1] - 1, guards[i][1] + 1, guards[i][0] - 1, guards[i][0] + 1
            
            while l >= 0:
                if (guards[i][0], l) not in st1 and (guards[i][0], l) not in st:
                    if not visited[guards[i][0]][l]:
                        guarded += 1
                        visited[guards[i][0]][l] = True
                    l -= 1
                else:
                    break
            
            while r < n:
                if (guards[i][0], r) not in st1 and (guards[i][0], r) not in st:
                    if not visited[guards[i][0]][r]:
                        guarded += 1
                        visited[guards[i][0]][r] = True
                    r += 1
                else:
                    break
            
            while u >= 0:
                if (u, guards[i][1]) not in st1 and (u, guards[i][1]) not in st:
                    if not visited[u][guards[i][1]]:
                        guarded += 1
                        visited[u][guards[i][1]] = True
                    u -= 1
                else:
                    break
            
            while d < m:
                if (d, guards[i][1]) not in st1 and (d, guards[i][1]) not in st:
                    if not visited[d][guards[i][1]]:
                        guarded += 1
                        visited[d][guards[i][1]] = True
                    d += 1
                else:
                    break
        
        return m * n - (len(guards) + len(walls) + guarded)
