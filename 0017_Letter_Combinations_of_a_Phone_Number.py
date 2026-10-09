# A dumb solution but better than nothing

class Solution:

    def letterCombinations(self, digits: str) -> list[str]:
        letter_mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        result = []

        if len(digits) == 1:
            return letter_mapping[digits[0]]
        elif len(digits) == 2:
            i = 0
            j = 0
            first = letter_mapping[digits[0]]
            second = letter_mapping[digits[1]]
            while i < len(first):
                while j < len(second):
                    result.append(first[i] + second[j])
                    j += 1
                i += 1
                j = 0
        elif len(digits) == 3:
            i = 0
            j = 0
            k = 0
            first = letter_mapping[digits[0]]
            second = letter_mapping[digits[1]]
            third = letter_mapping[digits[2]]
            while i < len(first):
                while j < len(second):
                    while k < len(third):
                        result.append(first[i] + second[j] + third[k])
                        k += 1
                    j += 1
                    k = 0
                i += 1
                j = 0
                k = 0
        else:
            i = 0
            j = 0
            k = 0
            m = 0
            first = letter_mapping[digits[0]]
            second = letter_mapping[digits[1]]
            third = letter_mapping[digits[2]]
            fourth = letter_mapping[digits[3]]
            while i < len(first):
                while j < len(second):
                    while k < len(third):
                        while m < len(fourth):
                            result.append(first[i] + second[j] + third[k] + fourth[m])
                            m += 1
                        k += 1
                        m = 0
                    j += 1
                    k = 0
                    m = 0
                i += 1
                j = 0
                k = 0
                m =0

        return result

