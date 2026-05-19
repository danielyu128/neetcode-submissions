class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in range(len(strs)):
            word = {}
            keyWord = ""
            for char in strs[i]:
                word[char] = 1 + word.get(char,0)
                keyWord = str(word)
            if keyWord not in groups:
                groups[keyWord] = []
            groups[keyWord].append(strs[i])
        return list(groups.values())
