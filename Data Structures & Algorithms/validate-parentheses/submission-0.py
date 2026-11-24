class Solution:
    def isValid(self, s: str) -> bool:
        closePair = {")": "(", "}": "{", "]": "["}

        stack = []

        for c in s:
            if c in closePair:
                if len(stack) > 0 and stack[-1] == closePair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        else:
            return False
