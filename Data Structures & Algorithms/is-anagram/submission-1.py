class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        times_appeared_s = {}
        times_appeared_t = {}

        for char in s:
            if char in times_appeared_s:
                times_appeared_s[char] = times_appeared_s[char] + 1
            elif char not in times_appeared_s:
                times_appeared_s[char] = 1

        for char in t:
            if char in times_appeared_t:
                times_appeared_t[char] = times_appeared_t[char] + 1
            elif char not in times_appeared_t:
                times_appeared_t[char] = 1

        return times_appeared_s == times_appeared_t