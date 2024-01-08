

from collections import deque 
class GridPoint:
    def __init__(self, x, y, grid):
        self.x = x 
        self.y = y 
        self.__n = len(grid)
        self.__m = len(grid[0])
        self.grid = grid 
    
    def __repr__(self):
        return f'({self.x}, {self.y})'

    def valid(self):
        return self.x >= 0 and self.x < self.__n and self.y >=0 and self.y < self.__m

    def land(self):
        return self.grid[self.x][self.y] == 1


class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        visited = [] 
        for i in range(len(grid)):
            visited.append([False] * len(grid[0]))
        
        def bfs(point, grid):   
            print(f'############# RUN of BFS for {point} ##########')  
            queue = deque()
            queue.append( point ) 
            island_area = 0 
            while( queue ):
                print(queue) 
                point = queue.popleft()
                if visited[point.x][point.y]:
                    continue 
                island_area += 1 
                visited[point.x][point.y] = True 
                point_a = GridPoint(point.x+1, point.y, grid)
                point_b = GridPoint(point.x-1, point.y, grid)
                point_c = GridPoint(point.x, point.y+1, grid)
                point_d = GridPoint(point.x, point.y-1, grid)
                if point_a.valid() and point_a.land():
                    if not visited[point_a.x][point_a.y]:
                        queue.append(point_a)
                if point_b.valid() and point_b.land():
                    if not visited[point_b.x][point_b.y]:
                        queue.append(point_b)
                if point_c.valid() and point_c.land():
                    if not visited[point_c.x][point_c.y]:
                        queue.append(point_c)
                if point_d.valid() and point_d.land():
                    if not visited[point_d.x][point_d.y]:
                        queue.append(point_d)
            return island_area

        result = []
        m = len(grid)
        n = len(grid[0])
        print('############# GRID ##########')
        for line in grid:
            print(line) 
        print('############# GRID ##########')

        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    ans = bfs(GridPoint(i, j, grid), grid)
                    print('############# VISITED ##########')
                    for line in visited:
                        print(line)
                    print('############# VISITED ##########')
                    result.append(ans)
        
        if len(result):
            return max(result)
        return 0 
    

if __name__=='__main__':
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    print(Solution().maxAreaOfIsland(grid))

