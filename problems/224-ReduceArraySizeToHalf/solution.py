
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        
        l = len(arr)
        if l == 1:
            return 1
        
        freq_map = Counter(arr)
        freq_map = {k: v for k, v in sorted(freq_map.items(), key=lambda item: -item[1])}
        
        res = 0
        half = l/2
        curr = 0
        for k, v in freq_map.items():
            if curr < half:
                curr += v
                res += 1
            else:
                break
        
            
        return res

#Optimized
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        
        l = len(arr)
        if l == 1:
            return 1
        
        freq_list = list(Counter(arr).values())
        freq_list.sort(reverse=True)
        
        res = 0
        half = l/2
        curr = 0
        for count in freq_list:
            if curr < half:
                curr += count
                res += 1
            else:
                break
        return res


