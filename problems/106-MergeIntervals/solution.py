class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])
        
        res = [intervals[0]]
        
        for idx in range(1,len(intervals)):
            cur = intervals[idx]
            last = res[-1]
            
            if last[1] < cur[0]:
                res.append(cur)
            else:
                last[1] = max(last[1], cur[1])
            
        return res
 
# class Solution:
# def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    
#     mapping  = defaultdict(int)
#     ans = []
    
#     for interval in intervals:
#         mapping[interval[0]] += 1
#         mapping[interval[1]] -= 1
    
        
#     startpt = -1 
#     endpt = -1
#     freq = 0
    
#     for key in sorted(mapping):
#         prevfreq = freq
#         freq += mapping[key]
        
#         if prevfreq == 0 and freq >0:
#             startpt = key  
#         if freq == 0:
#             endpt = key
#             if startpt == -1:
#                 startpt = endpt
            
#             ans.append([startpt, endpt])
#             startpt = endpt = -1
    
#     return ans