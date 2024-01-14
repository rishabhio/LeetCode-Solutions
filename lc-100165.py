


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int):
        one = len(s) - len(a) + 1 
        two = len(s) - len(b) + 1 
        potential_a = [] 
        potential_b = [] 
        beautiful = set()
        for i in range(0, one):
            if s[i: len(a)+i] == a:
                potential_a.append( i ) 
        for j in range(0, two):
            if s[j: len(b)+j] == b:
                potential_b.append( j )
        # print(potential_a)
        # print(potential_b) 
        for _a in potential_a:
            for _b in potential_b:
                if abs(_b - _a) <= k:
                    beautiful.add(_a)
        return sorted(list(beautiful))    

soln = Solution()
print(soln.beautifulIndices("isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15)) 

