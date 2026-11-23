class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            a = nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                s = a + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.add((a, nums[l], nums[r]))
                    l += 1
                    r -= 1

        return [list(x) for x in res]
