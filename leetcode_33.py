from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                pass
        return -1
s = Solution()
print(s.search([1,2,5,6,4,7], 10))