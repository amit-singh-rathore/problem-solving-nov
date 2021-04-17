class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [x for x in s]
        i, j = 0, len(s)-1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        while i<j:
            while s[i] not in vowels  and j>i:
                i += 1
            while s[j] not in vowels and j>i:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)