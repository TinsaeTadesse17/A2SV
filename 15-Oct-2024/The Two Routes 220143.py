# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

n , m = map(int,input().split())
edges = []
graph = [[] for i in range(n)]  
for i in range(m):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

    edges.append((a,b,1))
    edges.append((b,a,1))
roads = []
for i in range(n):
    for j in range(n):
        if i != j and j not in graph[i]:
            roads.append((i,j,1))


prev = [float("inf") for i in range(n)]
curr = [float("inf") for i in range(n)]
curr[0] = 0
prev[0] = 0

for i in range(n-1):
    for u,v,w in edges:
        curr[v-1] = min(curr[v-1],prev[u-1]+w)
    prev = curr.copy()


prev1 = [float("inf") for i in range(n)]
curr1 = [float("inf") for i in range(n)]
curr1[0] = 0
prev1[0] = 0

for i in range(n-1):
    for u,v,w in roads:
        curr1[v] = min(curr1[v],prev1[u]+w)
    prev1 = curr1.copy()



if curr1[-1] == float("inf") or curr[-1] == float("inf"):
    print(-1)
else:
    print(max(curr[-1],curr1[-1]))

