# 섬의 갯수를 구하는 문제 (1:땅, 0:물)

from collections import deque

def num_of_islands(grid):
    num_of_islands = 0
    row = len(grid)  
    col = len(grid[0])
    visited = [[False]*col for _ in range(row)]
    
    def bfs(x,y):
        visited[x][y] = True
        queue = deque()
        queue.append((x,y))
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if next_x >= 0 and next_x < row and next_y >=0 and next_y < col:
                    if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y)) 
    
    for x in range(row):
        for y in range(col):
            if not visited[x][y] and grid[x][y] == "1":
                bfs(x,y)
                num_of_islands += 1
    
    return num_of_islands




grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"],
]
print(num_of_islands(grid)) # 3