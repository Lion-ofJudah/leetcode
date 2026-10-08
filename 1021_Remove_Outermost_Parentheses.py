class Solution:

    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        i = 0
        start = 0
        end = 0
        stack = []
        while i < len(s):
            start = end + 1
            if s[i] == "(":
                stack.append(s[i])
            else:
                stack.pop()

            if len(stack) == 0:
                result += s[start:i]
                end = i + 1

            i += 1

        return result
        
