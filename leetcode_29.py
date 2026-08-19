class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)

        # Overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Same numbers
        if dividend == divisor:
            return 1

        # Determine whether result is negative
        negative = (dividend < 0) ^ (divisor < 0)

        # Convert both numbers to positive
        temp = abs(dividend)
        d = abs(divisor)

        ans = 0

        while temp >= d:
            cnt = 0

            while (d << (cnt + 1)) <= temp:
                cnt += 1

            temp -= (d << cnt)
            ans += (1 << cnt)

        # Apply sign
        if negative:
            ans = -ans

        return ans

s = Solution()
print(s.divide(10, 9))  # Output: 3