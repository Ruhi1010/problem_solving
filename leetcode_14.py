from typing import List
class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans = ""
        first = v[0]
        last = v[-1]
        
        for i in range(min(len(v[0]), len(v[-1]))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans
s = Solution()
print(f"Longest common prefix of ['flower','flow','flight'] = {s.longestCommonPrefix(['flower','flow','flight'])}")  # Output: "fl"
