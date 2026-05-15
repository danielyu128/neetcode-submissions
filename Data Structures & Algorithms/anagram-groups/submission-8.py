class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)

        for str in strs:

            chars = [0] * 26

            for c in str:
                chars[ord(c)-ord('a')] += 1

            grouped_anagrams[tuple(chars)].append(str)

        return list(grouped_anagrams.values())