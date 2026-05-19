class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_str_1, hash_str_2 = {},{}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hash_str_1[i] = hash_str_1.get(i,0) + 1
            hash_str_2[i] = hash_str_2.get(i,0) + 1

        if hash_str_1 == hash_str_2:
            return True
        return False
