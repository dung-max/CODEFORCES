from collections import deque

def bfs(n, adj):
    dist = [-1] * (n + 1)
    dist[1] = 0
    queue = deque([1])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist

def solve(n, m, k, product_types, roads):
    adj = [[] for _ in range(n + 1)]
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)
    
    dist_from_port = bfs(n, adj)

    max_dist = [0] * k
    for i in range(1, n + 1):
        product_type = product_types[i - 1]
        max_dist[product_type - 1] = max(max_dist[product_type - 1], dist_from_port[i])

    return max_dist

n, m, k = map(int, input().split())
product_types = list(map(int, input().split()))
roads = [tuple(map(int, input().split())) for _ in range(m)]

result = solve(n, m, k, product_types, roads)
print(*result)
