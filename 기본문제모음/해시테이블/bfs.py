# 그래프 bfs 기본 코드
from collections import deque

def bfs(graph, start_v):
    visited = [start_v]  # 방문한 노드 리스트
    queue = deque([start_v])  # 큐를 올바르게 초기화
    
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

graph = {
    'A' : ['B', 'D', 'E'],
    'B' : ['A', 'C', 'D'],
    'C' : ['B'],
    'D' : ['A', 'B'],
    'E' : ['A']
}

print(bfs(graph, 'A'))