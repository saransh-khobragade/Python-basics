# https://leetcode.com/problems/permutations-ii/
# Input: nums = [1,1,2]
# Output:[[1,1,2],[1,2,1],[2,1,1]]

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        
        if len(nums) == 1:
            return [nums]
        else:
            for i in range(len(nums)):
                for x in self.permute(nums[:i]+nums[i+1:]):
                    start = [nums[i]]
                    start.extend(x)
                    result.append(start)
        return result
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        arr = self.permute(nums)
        unique = set()
        result=[]
    
        for i in range(len(arr)):
            s = ''.join(list(map(str,arr[i])))

            if s not in unique:
                unique.add(s)
                result.append(arr[i])
                
        return result

    
s=Solution()
print(s.permuteUnique([1,1,2]))