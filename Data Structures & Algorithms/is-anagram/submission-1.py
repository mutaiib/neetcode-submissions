class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sourceMap = {}
        targetMap = {}
        
        for i in range(len(s)):
            if s[i] not in sourceMap:
                 sourceMap[s[i]] = 1
            else:
                sourceMap[s[i]] = sourceMap[s[i]] + 1
        
        for i in range(len(t)):
            if t[i] not in targetMap:
                 targetMap[t[i]] = 1
            else:
                targetMap[t[i]] = targetMap[t[i]] + 1

        for key in sourceMap:
            if key not in targetMap or targetMap[key] != sourceMap[key]:
                return False
        
        return True