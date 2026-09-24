class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]


class FollowUp:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_ind = {}
        for i in range(len(nums)):
            num = nums[i]
            other_pair = target - num
            if other_pair in num_ind:
                ind1 = num_ind[other_pair]
                return [ind1, i]

            num_ind[num] = i

