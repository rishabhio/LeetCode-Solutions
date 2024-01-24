



class Solution:

    def __init__(self):
        pass 

    def permute(self, nums):
        result = [] 
        def backtrack(start):
            if start == len(nums):
                result.append( nums.copy() ) 
                return 
            for i in range( start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start] 
                backtrack( start + 1 ) 
                nums[start], nums[i] = nums[i], nums[start] 

        backtrack(0) 
        return result 
    
if __name__ == '__main__':
    soln = Solution() 
    print(soln.permute( [1, 1] )) 