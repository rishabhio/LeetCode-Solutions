

import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True 
        def backtrack( num ):
            if num < 3:
                return False 
            elif num == 3:
                return True 
            return backtrack( num // 3 ) 
        return backtrack( n )
    
if __name__=='__main__':
    soln = Solution() 
    print(soln.isPowerOfThree( 27 )) 