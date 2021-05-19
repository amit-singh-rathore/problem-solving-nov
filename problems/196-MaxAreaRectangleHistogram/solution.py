class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hstack, pstack = [], []
        max_area = 0
        heights.append(0)
        for idx, ht in enumerate(heights):
            width = len(heights)+1
            while hstack and hstack[-1]> ht:
                width = pstack[-1]
                cur_area = (idx - pstack.pop()) * hstack.pop()
                max_area = max(cur_area, max_area)
            if not hstack or hstack[-1] < ht:
                hstack.append(ht)
                pstack.append(min(width, idx))
        return max_area
                
            