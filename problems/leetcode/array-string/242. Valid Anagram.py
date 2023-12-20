class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)

        if len(s) == len(t):
            for x in s:
                if x not in t:
                    return False
                else:
                    t.remove(x)
            return True
        else:
            return False
        
s = Solution()
print(s.isAnagram("aacc","ccac"))

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
"""