'''
    LC-1319 - Number of Operations to Make Network Connected

    Algo: Union Find 
    Type: Graph
    Author: Rishabh IO
    Language: Python3
    Time Complexity: O(n)
    Space Complexity: O(n)

    Reference: https://www.youtube.com/watch?v=Kptz-NVA2RE
    

'''

class Solution:

        def makeConnected(self, n: int, connections):
            parents = [ i for i in range(n)]

            def find(x):
                if parents[x] != x:
                    parents[x] = find(parents[x])
                return parents[x] 
            
            def union(a, b):
                root_a = find(a) 
                root_b = find(b) 
                if root_a == root_b:
                     return True 
                parents[root_a] = root_b
                return False 
            
            extra_edges = 0 
            for a, b in connections:
                if union(a, b):
                    extra_edges += 1
            
            components = 0 
            for i in range(n):
                 if i == find(i):
                    components += 1
            
            if extra_edges >= components - 1:
                return components - 1
            else:
                return -1
                
                   
if __name__ == "__main__":
    n = 4
    connections = [[0,1],[0,2],[1,2]]
    print(Solution().makeConnected(n, connections))