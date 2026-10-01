class Solution:

    def get_digits(self, num: int) -> dict:
        digits = {}
        i = 1
        while i < 5:
            digit = num % 10
            num = num // 10
            digits[i] = digit
            i += 1

        return digits

    def intToRoman(self, num: int) -> str:
        roman = ""
        num_digits = self.get_digits(num)
        thousands = num_digits[4]
        hundreds = num_digits[3]
        tens = num_digits[2]
        ones = num_digits[1]

        roman += "M" * thousands
        # calculate for hundreds place
        if hundreds != 4 and hundreds != 9:
            if hundreds >= 5:
                roman += "D"
                roman += "C" * (hundreds - 5)
            else:
                roman += "C" * hundreds
        else:
            if hundreds == 4:
                roman += "CD"
            else:
                roman += "CM"
        
        # calculate for tens place
        if tens != 4 and tens != 9:
            if tens >= 5:
                roman += "L"
                roman += "X" * (tens - 5)
            else:
                roman += "X" * tens
        else:
            if tens == 4:
                roman += "XL"
            else:
                roman += "XC"

        # calculate for ones place
        if ones != 4 and ones != 9:
            if ones >= 5:
                roman += "V"
                roman += "I" * (ones - 5)
            else:
                roman += "I" * ones
        else:
            if ones == 4:
                roman += "IV"
            else:
                roman += "IX"

        return roman
        
