import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]      
    
    
s = Solution()
input_str = str(input("Enter a string to check if it's a palindrome: "))
print(s.isPalindrome(input_str))  