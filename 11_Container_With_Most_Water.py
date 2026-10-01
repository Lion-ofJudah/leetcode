class Solution:

    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        max_water = 0
        while i != j:
            container = min(height[i], height[j])
            difference = j - i
            area = container * difference

            if area >= max_water:
                max_water = area
            
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1

        return max_water
        
