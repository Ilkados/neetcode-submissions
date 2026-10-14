class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l:int = 0 
        r:int = len(s)-1
        
        while(l<=r):

            while(not s[l].isalnum() and l < r):
                l+=1

            while(not s[r].isalnum() and r > l):
                r-=1
        
            if (s[l].upper() != s[r].upper()):
                return False
                
            r-=1
            l+=1
            
        return True