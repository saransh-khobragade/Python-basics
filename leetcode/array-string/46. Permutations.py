# https://leetcode.com/problems/permutations/
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
from typing import List
class Solution:
    def permuteUtil(self,arr,pos,size):
        result=[]
        if pos == size:
            return [[*arr]]
        else:
            for i in range(pos,size):
                arr[i],arr[pos] = arr[pos],arr[i]
                result.extend(self.permuteUtil(arr,pos+1,size))
                arr[i],arr[pos] = arr[pos],arr[i]
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permuteUtil(nums,0,len(nums))
        

        
s=Solution()
print(s.permute([1,2,3]))