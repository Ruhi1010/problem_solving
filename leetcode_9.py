class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        c = []
        a = []
        b = []

        for i in range(len(s)):
            a.append(s[i])
            c.append(s[i])
        for i in range(len(s)):
            p = a.pop()
            b.append(p)

        if b == c:
            return True
        else: 
            return False

s = Solution()
print(f"Is 12121 a palindrome? = {s.isPalindrome(12121)}")