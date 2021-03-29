class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        #initial direction is North, along Y-axis
        i_direction = direction = [0,1]
        i_pos = pos = [0,0]
        
        def get_inc_along_axes(instr, cur_dir):
            return([instr[0][0]*cur_dir[0]+instr[0][1]*cur_dir[1], instr[1][0]*cur_dir[0]+instr[1][1]*cur_dir[1]])
        
        L = [[0,-1], [1, 0]] 
        R = [[0, 1], [-1,0]]
        
        for inst in instructions:
            if inst == "G":
                pos = [pos[0]+direction[0], pos[1]+direction[1]]
            elif inst == "L":
                direction = get_inc_along_axes(L, direction)
            else:
                direction = get_inc_along_axes(R, direction)
        
        if pos == i_pos or direction != i_direction:
            return True
        return False