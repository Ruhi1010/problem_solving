from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxx = nums[0]

        for i in nums:
            total = max(total + i, i)
            maxx = max(maxx, total)
        
        return maxx

c = Solution()
print(c.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))