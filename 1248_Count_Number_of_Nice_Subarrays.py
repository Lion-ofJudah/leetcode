class Solution:

    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        result = 0
        odd_idxs = []

        for i in range(len(nums)):
            num = nums[i]

            if num % 2 != 0:
                odd_idxs.append(i)
        
        if len(odd_idxs) < k:
            return 0
        
        i = 0

        while i < len(odd_idxs):
            multiplier_left = 1
            multiplier_right = 1

            idx = odd_idxs[i]
            if i == 0:
                multiplier_left = idx + 1
            else:
                multiplier_left = idx - odd_idxs[i - 1]
            
            j = i + k - 1
            if i + k == len(odd_idxs):
                multiplier_right = len(nums) - odd_idxs[j]
                i += k
            else:
                multiplier_right = odd_idxs[i + k] - odd_idxs[j]
                i += 1
            result += multiplier_left * multiplier_right

        return result

