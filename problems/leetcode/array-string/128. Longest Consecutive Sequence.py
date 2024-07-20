from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        startToEnd = {}  #startToEnd-end
        endToStart = {}    #end-startToEnd
        l=0

        for x in nums:
            flag = False
            # if x in s:
            #     continue
            if x+1 in startToEnd:
                startToEnd[x] = startToEnd[x+1] 
                del startToEnd[x+1]
                
                if x in endToStart:
                    endToStart[startToEnd[x]] = endToStart[x]
                    startToEnd[endToStart[x]] = startToEnd[x]
                    del endToStart[x]
                # end[x+1] = x
                flag=True
            
            if x-1 in endToStart:
                endToStart[x] = endToStart[x-1]
                del endToStart[x-1]
                
                if x in startToEnd:
                    startToEnd[endToStart[x]] = startToEnd[x]
                    endToStart[startToEnd[x]] = endToStart[x]
                    del startToEnd[x]
                # startToEnd[x-1] = x
                flag=True

            if not flag:
                startToEnd[x]=x
                endToStart[x]=x

        print(l)

        
s = Solution()
s.longestConsecutive([100,4,200,1,3,2])