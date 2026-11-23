class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0] * n, [0] * n

        for i in range(1, n):
            left[i] = max(left[i - 1], height[i - 1])

        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i + 1])

        water = 0
        for i in range(n):
            water += max(0, min(left[i], right[i]) - height[i])
        return water
