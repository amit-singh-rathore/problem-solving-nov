class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n  for i in range(n)]
        top, bottom, left, right = 0, n-1, 0, n-1
        move=1
        elem = 1
        
        while left <= right and top <= bottom:
            if move==1:
                for i in range(left, right+1):
                    res[top][i] = elem
                    elem += 1
                top += 1
                
            elif move==2:
                for i in range(top, bottom + 1):
                    res[i][right] = elem
                    elem += 1
                right -= 1
            elif move==3:
                for i in range(right, left-1, -1):
                    res[bottom][i] = elem
                    elem += 1
                bottom -= 1
            else:
                for i in range(bottom, top-1, -1):
                    res[i][left] = elem
                    elem += 1
                left += 1;
            move += 1;
            
            move=move%4
    
        return res