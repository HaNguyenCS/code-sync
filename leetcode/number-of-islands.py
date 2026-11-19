from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        dir = [
            [1,0],
            [-1,0],
            [0,1],
            [0,-1]
        ]

        q = deque()
        visited = set()
        row = len(grid)
        col = len(grid[0])

        def bfs(r,c):
            q.append((r,c))
            while q:
                r,c = q.popleft()
                visited.add((r,c))
                for ro,co in dir:
                    nr=r+ro
                    nc=c+co
                    if (nr in range(row) and nc in range(col) and grid[nr][nc]=="1" and (nr,nc) not in visited):
                        q.append((nr,nc))
                        visited.add((nr,nc))

        count = 0
        for r in range(0,row):
            for c in range(0,col):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    count += 1
                
        return count