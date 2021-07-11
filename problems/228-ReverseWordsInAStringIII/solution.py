class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        idx = len(s)-1
        last_idx = len(s)

        def reverse(start, end):
            ret = ""
            while end >= start:
                ret += s[end]
                end -= 1
            return ret 

        start =  0
        end = 0
        res =  ""
        for idx in range(len(s)):
            if s[idx] == ' ':
                end = idx-1

                if len(res)>0:
                    res += ' ' + reverse(start, end)
                else:
                    res = reverse(start, end)
                start = idx+1
        if len(res)>0:
            res += ' ' + reverse(start, len(s)-1)
        else:
            res = reverse(start, len(s)-1)
        return res


# Simpler version
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i in range(len(words)):
            words[i] = words[i][::-1]

        return ' '.join(words)