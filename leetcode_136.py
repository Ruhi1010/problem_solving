from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        index = 0
        for num in nums:
            index ^= num
        return index
        
        
s = Solution()
# Example usage:
nums = [4,1,2,1,2]
result = s.singleNumber(nums)
print("The single number is:", result)