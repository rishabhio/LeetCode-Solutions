
'''
Problem: Product of Array Except Self
Source: https://leetcode.com/problems/product-of-array-except-self/
Author: Rishabh IO

Intuition: The idea behind this problem is simple, we've to calculate the 
            product of all the elements of the array except the current element. 

O(n) TC and O(n) SC solution is possible by using 2 arrays one for storing the 
left product and one for storing the right product. 

O(n) TC and O(1) SC solution is possible by using the output array itself to
store the left product and then using a variable to store the right product.


'''


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        lp = [1] * n 
        rp = [1] * n 
        products = [1] * n 
        lp[0] = nums[0]
        rp[n-1] = nums[n-1]
        for i in range(1, n):
            lp[i] = nums[i] * lp[i-1]
        for j in range(n-2, -1, -1):
            rp[j] = nums[j] * rp[j+1]
         
        products[0] = rp[1] 
        products[n-1] = lp[-2]
        for k in range(1, n-1):
            products[k] = lp[k-1] * rp[k+1]
        return products