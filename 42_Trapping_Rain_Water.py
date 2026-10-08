class Solution:

    def trap(self, height: list[int]) -> int:
        # forward pass
        i = 0
        j = 1
        temp = 0
        high = height[0]
        high_index = 0
        result = 0

        while i < len(height) and j < len(height):
            if height[j] >= height[i]:
                i = j
                result += temp
                temp = 0
            else:
                temp += height[i] - height[j]
            
            if height[j] >= high:
                high = height[j]
                high_index = j

            j += 1

        # backward pass
        m = len(height) - 1
        n = len(height) - 2

        while m >= high_index and n >= high_index:
            if height[n] >= height[m]:
                m = n
                result += temp
                temp = 0
            else:
                temp += height[m] - height[n]

            n -= 1

        return result
