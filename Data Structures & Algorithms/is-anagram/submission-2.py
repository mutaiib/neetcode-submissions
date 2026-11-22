class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charMap = {}

        for i in range(len(s)):
            charMap[s[i]] = 1 + charMap.get(s[i], 0)

        for i in range(len(t)):
            if t[i] not in charMap:
                return False
            
            charMap[t[i]] -= 1

            if charMap[t[i]] < 0:
                return False
        
        return True
        
