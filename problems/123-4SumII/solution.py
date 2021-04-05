class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sum_counter = {}
        res = 0
        
        for x in A:
            for y in B:
                if x+y in sum_counter:
                    sum_counter[x+y] += 1
                else:
                    sum_counter[x+y] = 1
        
        for x in C:
            for y in D:
                target = -(x+y)
                if target in sum_counter:
                    res += sum_counter[target]
        
        return res
                    
        