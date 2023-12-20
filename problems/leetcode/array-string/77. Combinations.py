# https://leetcode.com/problems/combinations/
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

from typing import List

class Solution:
    def combine(self,L,N):
        sol=[]
        def backtrack(comb,level,pos,N):
            if level == 0:
                sol.append(comb.copy())
                return
            else:
                for i in range(pos,N+1):
                    comb.append(i)
                    backtrack(comb,level-1,i+1,N)
                    comb.pop()
        backtrack([],L,1,N)
        return sol
s = Solution()
N=3
L=2
print(s.combine(L,N))
