class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        count = 1
        longest = 1

        numsS = sorted(nums)
        for i in range(1, len(numsS)):
            if numsS[i - 1] == numsS[i]:
                continue

            if numsS[i - 1] + 1 == numsS[i]:
                count += 1
            else:
                longest = max(count, longest)
                count = 1

        return max(count, longest)
