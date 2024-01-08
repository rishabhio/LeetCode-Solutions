

class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x) 
        root_y = self.find(y) 
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x 
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y 
            else:
                self.parent[root_y] = root_x 
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def count(self):
        return len(set(self.parent))
    
    def __repr__(self):
        return str(self.parent)
    
    def __len__(self):
        return len(self.parent)
    
    def __getitem__(self, i):
        return self.parent[i]
    
    def __setitem__(self, i, val):
        return self.parent.__setitem__(i, val)
    

                   
        