# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol=[]
        def backtrack(comb,start):
            if sum(comb) > target:
                return comb[:-1]
            elif sum(comb) == target:
                sol.append(comb.copy())
                return comb[:-1]
            else:
                for i in range(start,len(candidates)):
                    comb.append(candidates[i])
                    comb = backtrack(comb,i)
                return comb[:-1]
        backtrack([],0)
        return sol

s=Solution()
print(s.combinationSum([2,3,6,7],7))