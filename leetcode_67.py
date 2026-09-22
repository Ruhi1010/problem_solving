class Solution:
  def addBinary(self, a: str, b: str) -> str:
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
      if i >= 0:
        carry += int(a[i])
        i -= 1
      if j >= 0:
        carry += int(b[j])
        j -= 1
      s.append(str(carry % 2))
      carry //= 2

    return ''.join(reversed(s))


s = Solution()
input_a = input("Enter the first binary string: ")
input_b = input("Enter the second binary string: ")
result = s.addBinary(input_a, input_b)
print(f"The sum of the binary strings is: {result}")