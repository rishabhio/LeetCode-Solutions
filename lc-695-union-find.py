from typing import Any


class Point:

    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def is_valid(self, grid):
        return self.x >= 0 and self.x < len(grid) and self.y >= 0 and self.y < len(grid[0]) and grid[self.x][self.y] == 1

    def __gt__(self, other):
        if self.x > other.x:
            return True 
        elif self.x == other.x:
            return self.y > other.y
        return False 

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

class UnionFind:

    def __init__(self, points):
        self.parents = {} 
        for point in points:
            self.parents[point] = point 

    def find(self, point):
        if point != self.parents[point]:
            self.parents[point] = self.find(self.parents[point])
        return self.parents[point]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if root_a > root_b:
                self.parents[root_b] = root_a
            else:
                self.parents[root_a] = root_b
            

class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        vertices = set()
        edges = [] 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    point = Point(i, j) 
                    vertices.add( point ) 
                    p_right = Point(i, j+1)
                    if p_right.is_valid(grid):
                        edge = (point, p_right)
                        edges.append(edge)
                    p_bottom = Point(i+1, j)
                    if p_bottom.is_valid(grid):
                        edge = (point, p_bottom)
                        edges.append(edge)

        uf = UnionFind(vertices)
        print(uf.parents) 
        print(edges) 
        for edge in edges:
            uf.union(edge[0], edge[1])

        most_freq_parents = {} 
        for _, val in uf.parents.items():
            try:
                most_freq_parents[val] += 1 
            except:
                most_freq_parents[val] = 1 
        
        if not len(most_freq_parents):
            return 0 
        return max(most_freq_parents.values())

if __name__=='__main__':
    soln = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    for line in grid:
        print(line) 
    print(soln.maxAreaOfIsland(grid))



