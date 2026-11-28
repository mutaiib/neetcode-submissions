class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = float('inf')
        for s in strs:
            if len(s) < minLength:
                minLength = len(s)

        i = 0
        while i < minLength:
            for s in strs:
                # fix one string from the list of strings
                if strs[0][i] != s[i]:
                    return s[:i]
            
            i += 1

        return strs[0][:i]

