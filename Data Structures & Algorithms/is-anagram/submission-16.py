class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_str_1, hash_str_2 = {},{}

        if len(s) != len(t): return False

        for i in range(len(s)):
            hash_str_1[s[i]] = hash_str_1.get(s[i],0) + 1
            hash_str_2[t[i]] = hash_str_2.get(t[i],0) + 1

        return hash_str_1 == hash_str_2
