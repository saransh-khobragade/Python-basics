# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
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
s=Solution()
print(s.permute([1,1,2]))