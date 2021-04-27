class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left , right = 0, len(needle)
        
        if len(needle) > len(haystack):
            return -1
        if len(needle)==0:
            return 0
        
        while right <= len(haystack):
            print(haystack[left:right])
            if haystack[left:right]== needle:
                return left
            else:
                left +=1
                right +=1
        return -1