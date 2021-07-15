class Solution:
    def customSortString(self, order: str, str: str) -> str:
        freq_count = Counter(str)
        seen = set()
        res = ""
        for item in order:
            if freq_count.get(item):
                seen.add(item)
                for _ in range(freq_count.get(item)):
                    res += item
                    
        for i in freq_count:
            if i not in seen:
                for _ in range(freq_count[i]):
                    res += i
        
        return res
                
        