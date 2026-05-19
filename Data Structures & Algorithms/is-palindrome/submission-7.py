class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            j = len(s)-1-i
            if s[i].isalnum and s[j].isalnum:
                if s[i].isalnum != s[j].isalnum:
                    return False
            if s[i].isalnum == False:
                continue
            elif s[j].isalnum == False:
                j-=1
        return True
