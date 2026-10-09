class Solution:

    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        
        i = 0
        interval = (2 * numRows) - 2
        j = interval
        result = s[i]

        while i < numRows:
            if j < len(s):
                if i != 0 and i != numRows - 1:
                    ind = j - (2 * i)
                    result += s[ind]

                result += s[j]
                j += interval
            else:
                if j - (2 * i) < len(s) and j - (2 * i) != j - interval:
                    ind = j - (2 * i)
                    result += s[ind]

                i += 1
                if i < numRows:
                    result += s[i]

                j = i + interval

        return result

