class Solution:
    def judgeCircle(self, moves: str) -> bool:
#         direction = {"L": (1,0), "R": (-1, 0), "U": (0,1), "D":(0,-1)}
        
#         init = [0, 0]
#         pos = [0, 0]
#         for char in moves:
#             move = direction[char]
#             pos = [pos[0]+move[0], pos[1]+move[1]]
#         if pos == init:
#             return True
#         else:
#             return False
        
        x = y = 0
        for char in moves:
            if char == 'L':
                x -= 1
            elif char == 'R':
                x += 1
            elif char == 'U':
                y += 1
            else:
                y -= 1
        return x==0 and y==0