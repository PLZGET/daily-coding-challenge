# 그래프 bfs 기본 코드

graph = {
    'A' : ['B', 'D', 'E'],
    'B' : ['A', 'C', 'D'],
    'C' : ['B'],
    'D' : ['A', 'B'],
    'E' : ['A']
}
visited = []
def dfs(cur_v):
    visited = [cur_v]
    for v in graph[cur_v]:
        if v not in visited:
            dfs(v)
            
    return visited