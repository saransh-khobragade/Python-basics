# https://leetcode.com/problems/string-compression/
"""
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 6 characters of the input array should be: ["a","b","1","2"]
"""
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        current = chars[0]
        count = 1
        d=[]
        for i in range(1,len(chars)):
            if current == chars[i]:
                count+=1
            else:
                d.append([current,count])
                current = chars[i]
                count = 1
        d.append([current,count])

        i=0
        for x,y in d:
            chars[i]=x
            i+=1
            if y>1:
                s = list(str(y))
                for z in s:
                    chars[i]=z
                    i+=1
        return i


s= Solution()
s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])

# Note : for changing 


"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
"""
