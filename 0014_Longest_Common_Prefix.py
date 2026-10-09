class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
        output = strs[0]

        for i in range(1, len(strs)):
            word = strs[i]
            output = output if len(output) <= len(word) else output[:len(word)]

            for j in range(len(output)):
                if word[j] == output[j]:
                    continue
                else:
                    output = output[:j]
                    break
            
            if len(output) == 0:
                break

        return output

