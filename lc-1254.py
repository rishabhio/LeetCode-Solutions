'''
    LC-1254 - Number of Closed Islands
    Type: Graph 
    Approach: BFS
    Author: Rishabh IO 
'''




class Point:

    def __init__(self, x, y, grid):
        self.x = x 
        self.y = y 
        self.x_len = len(grid)
        self.y_len = len(grid[0])
        self.grid = grid 

    def is_valid(self):
        if self.x >= 0 and self.y >= 0 and self.x < self.x_len and self.y < self.y_len and self.grid[self.x][self.y] == 0:
            return True
        return False 

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count_islands = 0 
        def bfs( point, COLOR ):
            queue = [ point ]
            while( queue ):
                point = queue.pop(0) 
                if point.is_valid():
                    grid[point.x][point.y] = COLOR
                    x = point.x 
                    y = point.y 
                    queue.append( Point(x-1, y, grid) )
                    queue.append( Point(x+1, y, grid) )
                    queue.append( Point(x, y+1, grid) )
                    queue.append( Point(x, y-1, grid) )
        # Run BFS on the extremes 
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            if grid[i][0] == 0:
                point = Point(i, 0, grid)
                bfs(point, 2)
            if grid[i][m-1] == 0:
                point = Point(i, m-1, grid)
                bfs(point, 2) 
        for j in range(m):
            if grid[0][j] == 0:
                point = Point(0, j, grid)
                bfs(point, 2)
            if grid[n-1][j] == 0:
                point = Point(n-1, j, grid)
                bfs(point, 2)

        # Run BFS on the remaining part of the Grid 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    count_islands += 1 
                    point = Point(i, j, grid)
                    bfs(point, 3) 
        return count_islands 