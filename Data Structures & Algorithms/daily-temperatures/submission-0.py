class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        output = [0] * n

        for i in range(n):
            while stack and temperatures[i] > stack[-1][0]:
                st, si = stack.pop()
                output[si] = (i - si)
            stack.append([temperatures[i], i])

        return output


