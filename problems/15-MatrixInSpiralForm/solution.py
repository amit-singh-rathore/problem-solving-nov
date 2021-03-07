def print_spiral(matrix, top_row_idx, bottom_row_idx, left_col_idx, right_col_idx):
    
    if (left_col_idx > right_col_idx): 
        return
    
    # print items for top row (rightward movement)
    for idx in range(left_col_idx, right_col_idx+1): 
        print(matrix[top_row_idx][idx], end=' ')
    
    top_row_idx += 1 #set the next top row
    
    if top_row_idx > bottom_row_idx:
        return
    
    # print items for right column (downward movement)
    for idx in range(top_row_idx, bottom_row_idx+1): 
        print(matrix[idx][right_col_idx], end=' ')
    
    right_col_idx -= 1 # set next right col
 
    if left_col_idx > right_col_idx:
        return
    
    # print item for bottom row (leftward movement)
    for idx in range(right_col_idx, left_col_idx - 1, -1): 
        print(matrix[bottom_row_idx][idx], end=' ') 
    
    bottom_row_idx -= 1 #set next bottom row 
 
    if top_row_idx > bottom_row_idx:
        return
    
    #print item for left column (upward movement)
    for idx in range(bottom_row_idx, top_row_idx-1, -1): 
        print(matrix[idx][left_col_idx], end=' ') 
    
    left_col_idx += 1 #set next left col
  
    print_spiral(matrix, top_row_idx, bottom_row_idx, left_col_idx, right_col_idx) 
    

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print_spiral(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1)
    