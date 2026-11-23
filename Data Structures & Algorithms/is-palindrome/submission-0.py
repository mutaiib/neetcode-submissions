class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = set("abcdefghijklmnopqrstuvwxyz0123456789")
        left, right = 0, len(s) - 1
        s = s.lower()

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] not in valid:
                left += 1
            elif s[right] not in valid:
                right -= 1
            else:
                return False

        return True
