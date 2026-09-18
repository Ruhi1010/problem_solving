

class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits
    
    
s = Solution()
input_digits = input("Enter a list of digits separated by spaces: ")
digits_list = [int(digit) for digit in input_digits.split()]
print(s.plusOne(digits_list))