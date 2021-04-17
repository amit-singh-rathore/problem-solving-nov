class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub('[^0-9A-Za-z]', '', s.lower())
        i, j = 0, len(s)-1
        while i<j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
        