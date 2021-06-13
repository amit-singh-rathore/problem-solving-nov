# Faster
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s):
            return s == s[::-1]
        
        i, j = 0, len(s)-1
        while i < j:
            if s[i]!=s[j]:
                return helper(s[i:j]) or helper(s[i+1 : j+1]) 
            else:
                i += 1
                j -= 1
        return True
        
# Memory efficient
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def helper(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True
        

        i, j = 0, len(s)-1
        while i < j:
            if s[i]!=s[j]:
                return helper(s, i+1, j) or helper(s, i, j-1) 
            else:
                i += 1
                j -= 1
        return True