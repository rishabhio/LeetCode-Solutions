
'''
    LC-997 - Find the Town Judge
    Algo: Graph / HashMap 
    Type: Graph
    Language: Python3
    Author: Rishabh IO
    Notes: TC can be further improved, this is not 
    the most optimal solution.

'''

from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust):
        potential_judges = [ True ] * (n + 1)

        trustees = defaultdict(set) 
        for t in trust:
            eliminate = t[0]
            trustees[t[1]].add( eliminate )
            potential_judges[eliminate] = False 

        judge = -1
        for i in range( 1, n+1):
            if potential_judges[i] != False:
                judge = i 
        
        if judge == -1:
            return judge 
        
        # validate whether everybody trusts the judge:
        for i in range( 1, n ):
            if i == judge:
                continue 
            if i not in trustees[judge]:
                return -1 
        return judge 