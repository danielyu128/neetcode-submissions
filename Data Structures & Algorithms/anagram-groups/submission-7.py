class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in range(len(strs)):
            word = {}
            keyWord = ""
            sortedKeyword = ""
            for char in strs[i]:
                word[char] = 1 + word.get(char,0)
                keyWord = str(word)
                sortedKeyword = "".join(sorted(keyWord))
            if sortedKeyword not in groups:
                groups[sortedKeyword] = []
            groups[sortedKeyword].append(strs[i])
        return list(groups.values())
