from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        
        for x in nums:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        # sorting dictonary by its values
        out = sorted(dic.items(), key=lambda x:x[1] ,reverse=True)
        
        result = list(map(lambda x:x[0],out))

        return result[:k]


s = Solution()
nums = [1,1,1,2,2]
k=2
print(s.topKFrequent(nums,k))

