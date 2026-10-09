class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        if len(s) == 1:
            return 1
        
        result = 0
        i = 0
        j = 1
        temp = ""

        while i < len(s) and j < len(s):
            if temp == "":
                temp += s[i]

            substring = temp
            if s[j] in substring:
                i += 1
                j = i + 1
                temp = ""
                if len(substring) > result:
                    result = len(substring)
            else:
                substring += s[j]
                temp = substring
                j += 1

        return result if result > len(temp) else len(temp)

