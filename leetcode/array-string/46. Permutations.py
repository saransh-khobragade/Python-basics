# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol=[]

        def backtrack(comb,start):
            if start == len(nums):
                sol.append(comb.copy())
                return comb[:-1]
            else:
                for i in range(start,len(nums)):
                    comb.append(nums[i])
                    comb = backtrack(comb,i+1)
                return comb
        backtrack([],0)
        return sol

s=Solution()
print(s.permute([1,2,3]))