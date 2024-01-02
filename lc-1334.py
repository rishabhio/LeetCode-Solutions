
'''
    LC: 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
    Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
    Algo: Floyd-Warshall
    Type: Graph
    Author: Rishabh IO
    Language: Python3 
    Intuition: 
        - Find the shortest path between all pairs of nodes using Floyd-Warshall
        - For each node, count the number of nodes that are reachable within the distanceThreshold
        - Return the node with the smallest number of reachable nodes
    Intuition behind Floyd-Warshall:
        - https://www.youtube.com/watch?v=prx1psByp7U
    Time Complexity: O(n^3)
    Space Complexity: O(n^2)
'''

import math
class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        matrix = [] 
        for i in range(n):
            tmp = [] 
            for j in range(n):
                if i == j:
                    tmp.append(0)
                else:
                    tmp.append(math.inf)
            matrix.append( tmp ) 
        for edge in edges:
            frm = edge[0]
            to = edge[1]
            dis = edge[2]
            matrix[frm][to] = dis 
            matrix[to][frm] = dis

        

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])


        result = [0, math.inf]
        for i in range(n):
            tmp = 0 
            for j in range(n):
                if matrix[i][j] <= distanceThreshold and i!=j:
                    tmp += 1 
            if tmp <= result[1]:
                result[1] = tmp 
                result[0] = i 

        return result[0]
    
if __name__ == "__main__":
    n = 5
    edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
    distanceThreshold = 2
    print(Solution().findTheCity(n, edges, distanceThreshold))