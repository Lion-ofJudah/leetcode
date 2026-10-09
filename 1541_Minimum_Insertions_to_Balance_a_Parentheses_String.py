class Solution:

    def minInsertions(self, s: str) -> int:
        result = 0
        ctr = 0
        i = 0
        stack = []

        while i < len(s):
            print(result)
            b = s[i]
            if i == 0:
                if b == "(":
                    stack.append(b)
                else:
                    ctr += 1
                i += 1
                continue
            
            if b == "(":
                if s[i - 1] == ")":
                    if ctr == 1:
                        if len(stack) == 0:
                            result += 2
                        else:
                            result += 1
                            stack.pop()
                    ctr = 0
                stack.append(b)
            else:
                ctr += 1
                if ctr == 2:
                    if len(stack) == 0:
                        result += 1
                    elif len(stack) != 0:
                        stack.pop()
                    ctr = 0

            i += 1
        
        if ctr == 1:
            if len(stack) != 0:
                result += 1
                stack.pop()
                ctr = 0
            else:
                result += 2

        if len(stack) != 0 and ctr == 0:
            result += len(stack) * 2

        return result

