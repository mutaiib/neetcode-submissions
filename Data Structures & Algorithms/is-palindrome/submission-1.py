class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = set("abcdefghijklmnopqrstuvwxyz0123456789")
        left, right = 0, len(s) - 1
        s = s.lower()

        while left < right:
            while left < right and s[left] not in valid:
                left += 1

            while left < right and s[right] not in valid:
                right -= 1

            if s[left] != s[right]:
                return False

            left, right = left + 1, right - 1
        return True
