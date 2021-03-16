def maxArea(height):
    l = 0
    r = len(height) -1
    container_size = 0
    while l < r:
        left_boundary = height[l]
        right_boundary = height[r]
        if left_boundary < right_boundary:
            container_size = max(container_size, left_boundary * (r-l))
            l += 1
        else:
            container_size = max(container_size, right_boundary * (r-l))
            r -= 1
    
    
    return container_size