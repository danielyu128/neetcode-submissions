class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in range(len(strs)):
            word = {}
            for char in strs[i]:
                word[char] = 1 + word.get(char,0)
            if word not in groups:
                groups[word] = []

            groups[word].append(strs[i])
        return groups.values()
