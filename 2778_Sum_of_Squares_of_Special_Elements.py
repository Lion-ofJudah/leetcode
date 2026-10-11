class Solution:

    def sumOfSquares(self, nums: list[int]) -> int:
        result = 0
        i = 0
        while i < len(nums):
            if len(nums) % (i + 1) == 0:
                result += nums[i] ** 2
            
            i += 1
        
        return result
        
