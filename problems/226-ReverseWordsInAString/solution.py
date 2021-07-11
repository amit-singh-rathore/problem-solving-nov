class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        idx = len(s)-1
        last_idx = len(s)
        
        chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        prev_char = False
        for idx in range(len(s)-1, -1, -1):
            if s[idx] in chars:
                prev_char = True
                continue
            else:
                if prev_char:
                    res += ' ' + s[idx+1:last_idx]
                last_idx = idx
                prev_char = False
        if prev_char:
            res += ' ' + s[0:last_idx]
        return res.strip()