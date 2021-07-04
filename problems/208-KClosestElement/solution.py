# Linear Time using deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = deque(arr)
        while len(res) > k:
            res.pop() if abs(res[0]-x) <= abs(res[-1]-x) else res.popleft()
        
        return res

# Binary search to find closet element & Two pointer to find k element
from bisect import bisect, bisect_left

class Solution:
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        pos = bisect_left(arr, x)

        if pos == n:
            pos -= 1
            
        if pos> 0 and ((arr[pos] - x) >= (x - arr[pos-1])):
            pos -= 1

        l, r = pos, pos
        
        for i in range(k-1):
            if l == 0: 
                r += 1
            elif r == n-1: 
                l -= 1
            else:
                if (arr[r+1]-x) >= (x -arr[l-1]):
                    l -= 1
                else:
                    r += 1

        return arr[l:r+1]

# Binary Search
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        res_idx = 0 
        l, r = 0, n - k
        while l <= r:
            mid = (l + r) >> 1
            if mid+k == n or x - arr[mid] <= arr[mid+k] - x:
                res_idx = mid
                r = mid - 1
            else:
                l = mid + 1
        return arr[ res_idx : res_idx + k ]
        
