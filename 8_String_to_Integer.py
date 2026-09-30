class Solution:

    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0
        digits_read = 0
        i = 0
        while i < len(s):
            character = s[i]
            if not character.isdigit() and character != " " and character != "-" and character != "+":
                break
            
            if not character.isdigit() and digits_read > 0:
                break
            
            if character == "-":
                sign = -1
                digits_read += 1
            if character == "+":
                digits_read += 1
            
            if character.isdigit():
                result = result * 10 + ord(character) - 48
                digits_read += 1

            i += 1
        
        result *= sign
        if result > 2147483647:
            result = 2147483647
        elif result < -2147483648:
            result = -2147483648

        return result
        
