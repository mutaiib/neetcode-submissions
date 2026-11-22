class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difs = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in difs:
                return [difs[difference], i]

            difs[nums[i]] = i

        return []
