class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = "".join(filter(str.isalnum,s))

        for i in range(math.ceil(len(cleaned)/2)):
            j = len(cleaned) - 1 - i
            if cleaned[i] != cleaned[j]:
                return False
        return True