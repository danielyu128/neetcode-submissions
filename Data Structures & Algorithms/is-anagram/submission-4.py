class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_s, hash_t = {}, {}

        for char in s:
            hash_s[char] = 1 + hash_s[hash_s.get(char,0)]
            hash_t[char] = 1 + hash_t[hash_t.get(char,0)]

        return hash_s == hash_t