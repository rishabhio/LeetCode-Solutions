class Solution:
    def threeSum(self, nums):
        triplets = [] 
        
        nums = sorted(nums)
        print(nums)
        N = len(nums)
        for i in range(N):
            if i != 0 and nums[i] == nums[i-1]:
                continue 
            if nums[i] == 0:
                print('here') 
            target = -1 * nums[i]
            j = i + 1 
            k = N - 1 
            last_j = None 
            last_k = None 
            while( j < k ):
                print(f'i: {i}, j: {j}, k: {k}')
                if nums[j] == last_j and (k < N-1) and nums[k] == last_k:
                    j += 1 
                    k -= 1 
                    continue 
                if nums[j] + nums[k] == target:
                    triplets.append([nums[i], nums[j], nums[k]])
                    last_j = nums[j]
                    last_k = nums[k]
                    j += 1 
                    k -= 1 
                elif nums[j] + nums[k] < target:
                    j += 1 
                elif nums[j] + nums[k] > target:
                    k -= 1 
        return triplets
    
soln = Solution() 
nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
print(soln.threeSum(nums))