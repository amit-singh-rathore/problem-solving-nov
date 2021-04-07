class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        top, bottom, left, right = 0, n-1, 0, m-1
        move=1
        visited = []
        
        while left <= right and top <= bottom:
            if move==1:
                for i in range(left, right+1):
                    visited.append(matrix[top][i])
                top += 1
                
            elif move==2:
                for i in range(top, bottom + 1):
                    visited.append(matrix[i][right])
                right -= 1
            elif move==3:
                for i in range(right, left-1, -1):
                    visited.append(matrix[bottom][i])
                bottom -= 1
            else:
                for i in range(bottom, top-1, -1):
                    visited.append(matrix[i][left])
                left += 1;
            move += 1;
            
            move=move%4
    
        return visited
        