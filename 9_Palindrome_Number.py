class Solution:

    def isPalindrome(self, x: int) -> bool:
        result = 0
        temp = x
        while temp > 0:
            digit = temp % 10
            result = result * 10 + digit
            temp = temp // 10
        
        return result == x
        
