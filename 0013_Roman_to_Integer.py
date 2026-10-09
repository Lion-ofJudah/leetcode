class Solution:

    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        for i in range(len(s)):
            if i < len(s) - 1 and symbols[s[i]] < symbols[s[i + 1]]:
                result -= symbols[s[i]]
            else:
                result += symbols[s[i]]

        return result

    def romanToInt2(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        i = len(s) - 1
        previous = ""
        while i >= 0:
            character = s[i]
            if character == "I":
                if previous == "V" or previous == "X":
                    result -= symbols[character]
                else:
                    result += symbols[character]
            elif character == "X":
                if previous == "L" or previous == "C":
                    result -= symbols[character]
                else:
                    result += symbols[character]
            elif character == "C":
                if previous == "D" or previous == "M":
                    result -= symbols[character]
                else:
                    result += symbols[character]
            else:
                result += symbols[character]

            previous = character
            i -= 1

        print(symbols)

        return result

