class Solution:

    def isValid(self, s: str) -> bool:
        valid_pair = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for b in s:
            if b == "(" or b == "[" or b == "{":
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if valid_pair[b] != stack.pop():
                        return False
        
        return len(stack) == 0

