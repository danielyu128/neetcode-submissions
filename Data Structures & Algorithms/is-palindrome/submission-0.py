class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = "".join(filter(str.isalnum(),s))

        for i in range(math.ceil(len(s)/2)):
            j = len(s) - 1 - i
            if s[i] != s[j]:
                return False
        return True