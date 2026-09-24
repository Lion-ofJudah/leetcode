class Solution:

    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num: int = nums[i]
            sum: int = 0

            while num > 0:
                digit: int = num % 10
                num = int(num / 10)
                sum += digit

            if sum == i:
                return i

        return - 1

