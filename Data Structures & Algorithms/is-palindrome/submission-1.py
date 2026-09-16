class Solution:
    def isPalindrome(self, s: str) -> bool:
            cleaned = ''.join(c.lower() for c in s if c.isalnum())
            if (cleaned != cleaned[::-1]):
                return False
            return True 
