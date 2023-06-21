from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequency = set()
        for x in nums:
            if x in frequency:
                return True
            else:
                frequency.add(x)
        
        return False


nums = [1,2,3,4]
a = Solution()

print(a.containsDuplicate(nums))


"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Input: nums = [1,2,3,1]
Output: true
"""