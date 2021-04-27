class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==0:
            return -1
        if len(s)==1:
            return 0
        
        freq_map = Counter(s) 
        for idx, char in enumerate(s):
            if freq_map[char] == 1:
                return idx
        return -1