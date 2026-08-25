from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: If the list is empty, return 0
        if not nums:
            return 0
        
        # 'i' tracks the position of the last unique element found
        i = 0
        
        # 'j' scans through the rest of the array starting at index 1
        for j in range(1, len(nums)):
            # When we find a new unique element
            if nums[j] != nums[i]:
                i += 1          # Move the unique pointer forward
                nums[i] = nums[j] # Overwrite the next spot with the new unique value
        
        # Return the number of unique elements (index + 1)
        return nums[:i + 1]
    

s = Solution()
# Example usage:
nums = [0,0,1,1,1,2,2,3,3,4]
length = s.removeDuplicates(nums)
print("Length of unique elements:", length)