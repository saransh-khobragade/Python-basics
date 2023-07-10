# https://leetcode.com/problems/combinations/
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

from typing import List

class Solution:
    def combine(self,n,k):
        sol=[]
        def backtrack(level,comb,pos):
            if level == 0:
                sol.append(comb.copy())
                return
            else:
                for i in range(pos,n+1):
                    comb.append(i)
                    backtrack(level-1,comb,i+1)
                    comb.pop()
        backtrack(k,[],1)
        return sol
s = Solution()
n=3
k=2
print(s.combine(n,k))
