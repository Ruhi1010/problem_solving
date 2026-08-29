from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

            if nums[i] > target:
                return i

        return len(nums)
    

s = Solution()
# Example usage:
nums = [1, 3, 5, 6]
target = 5
result = s.searchInsert(nums, target)
print("The index of the target value in the array is:", result)