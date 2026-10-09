class Solution:

    def reverse(self, x: int) -> int:
        is_negative = x < 0
        if is_negative:
            x *= -1
        
        result = 0
        while x > 0:
            digit = x % 10
            result += digit
            x = x // 10
            if x > 0:
                result *= 10
        
        if result > (1 << 31) - 1:
            result = 0

        if is_negative:
            result *= -1
        
        return result

