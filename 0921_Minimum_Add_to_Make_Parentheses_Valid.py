class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        result = []
        i = 0

        while i < len(s):
            if s[i] == ")":
                if not len(result) or result[-1] == ")":
                    result.append(s[i])
                else:
                    result.pop()
            else:
                result.append(s[i])
            
            i += 1
        
        return len(result)
        
