# https://leetcode.com/problems/product-of-array-except-self/
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        products = [1]*l

        left=1
        for i in range(1,l):
            products[i]=nums[i-1] * left
            left =products[i]
        
        print(products)
        right = 1
        for i in range(l-1,-1,-1):
            products[i] *= right
            right *= nums[i]
        
        return products
        
        
s = Solution()
print(s.productExceptSelf([2,3,5,0]))
            