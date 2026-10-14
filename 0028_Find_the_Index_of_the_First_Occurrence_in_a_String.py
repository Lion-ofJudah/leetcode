class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        ln = len(needle)

        while i < len(haystack):
            w = i + ln
            if w > len(haystack):
                break

            if haystack[i : w] == needle:
                return i
            
            i += 1

        return -1

