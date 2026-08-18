from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = {}
        left = 0
        result = 0
        for right in range(len(s)):
            if s[right] in substring:
                left = max(substring[s[right]]+1,left)
            substring[s[right]] = right
            result=max(right - left + 1, result)
        return result
    
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))