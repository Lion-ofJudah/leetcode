class Solution:

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        result = ""
        temp = ""
        i = 0
        j = 1
        while i < len(s):
            if temp == "":
                temp += s[i]
                if len(result) < len(temp):
                    result = temp

            if j < len(s):
                temp += s[j]
                if s[i] == s[j]:
                    pal = self.is_palindrome(temp)
                    if pal and len(result) < len(temp):
                        result = temp
                  
                j += 1
            else:
                i += 1
                j = i + 1
                temp = ""

        return result

