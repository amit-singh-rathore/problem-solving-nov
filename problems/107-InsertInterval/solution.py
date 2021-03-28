class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        strt, end = newInterval[0], newInterval[1]
        n = len(intervals)
        idx = 0
        # find the place where it will inserted 
        while idx < n and strt > intervals[idx][1]:
            idx += 1
        i = idx

        #keep finding updating the start and end if they overlap
        while (i < n) and (strt <= intervals[i][1]) and (intervals[i][0] <= end):
            strt = min(strt, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        return intervals[ : idx] + [[strt, end]] + intervals[i : ]