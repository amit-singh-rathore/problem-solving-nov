class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        char_set = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        
        start = 0
        end = 0
        prev_char = False
        for idx , value in enumerate(s):
            if value in char_set:
                if not prev_char:
                    start = idx
                prev_char = True
            else:
                if prev_char:
                    end = idx-1
                    reverse(start, end)
                    prev_char = False
                    
        reverse(start, len(s)-1)
        
        start , end = 0, len(s)-1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1