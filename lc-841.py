
'''
    841. Keys and Rooms
    Source: https://leetcode.com/problems/keys-and-rooms/

    Algo: BFS 
    Type: Graph

    Notes: This is a simple BFS problem.
    Author: Rishabh IO
'''

class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        n = len( rooms ) 
        locked = [ True ] * n 
        locked[ 0 ] = False 
        visited = set()
        queue = [ 0 ] 

        while( queue ):
            room = queue.pop(0)
            visited.add( room )
            locked[room] = False 
            for key in rooms[room]:
                if key not in visited:
                    queue.append( key ) 

        if any(locked):
            return False 
        return True 