class Solution:
    def isPalindrome(self, s: str) -> bool:
            cleaned = ''.join(c.lower() for c in s if c.isalnum())
            copy = cleaned
            if (cleaned != copy[::-1]):
                return False
            return True 
