class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        left_boundary = [-1]*n
        right_boundary = [-1]*n
        left_boundary[0] = height[0]
        right_boundary[-1] = height[-1]
        
        for i in range(1, n):
            left_boundary[i] = max(left_boundary[i-1], height[i])
        
        for i in range(n-2, -1, -1):
            right_boundary[i] = max(right_boundary[i+1], height[i])
        
        res = 0
        
        for i in range(n):
            if left_boundary[i] != height[i] and right_boundary[i] != height[i]:
                res += min(left_boundary[i], right_boundary[i]) - height[i]
        
        return res