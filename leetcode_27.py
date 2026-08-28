from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         index = 0
         for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
         return index
     
     

s = Solution()
# Example usage:
nums = [3, 2, 2, 2, 2, 3, 5]
val = 3
result = s.removeElement(nums, val)
print("The new length of the array after removing the value is:", result)