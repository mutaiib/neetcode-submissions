class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in range(len(strs)):
            count = [0] * 26
            for char in strs[i]:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)

            if key not in groups:
                groups[key] = []

            groups[key].append(strs[i])

        return list(groups.values())