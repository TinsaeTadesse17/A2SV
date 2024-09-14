# Problem: B - Path Finder - https://codeforces.com/gym/517685/problem/B

n = int(input())  
edges = []
for _ in range(n - 1):
    u, v, c = map(int, input().split())
    edges.append((u, v, c))

adj = [[] for _ in range(n)]

for u, v, c in edges:
    adj[u].append((v, c))
    adj[v].append((u, c))

visited = [False] * n

def dfs(node, adj, visited):
    visited[node] = True
    ans = 0
    
    for neighbor, weight in adj[node]:
        if not visited[neighbor]:
            ans = max(ans, dfs(neighbor, adj, visited) + weight)
    
    return ans

print(dfs(0, adj, visited))
