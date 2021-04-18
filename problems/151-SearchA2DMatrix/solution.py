class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search within a row elements
        def binary_search(array , left , right , target):
            while left <= right:
                mid = (left+right)//2
                if array[mid] == target:
                    return True
                elif array[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return False
        
        row = 0
        row_max = len(matrix)-1
        col_max = len(matrix[0])-1
        
        if row_max == 0 and col_max == 0:
            return matrix[0][0] == target
        
        if target < matrix[0][0] or target > matrix[row_max][col_max]:
            return False
        
        res = False
        
        #Binary search for finding which row to search in
        i , j = 0, row_max
        while i < j:
            mid = (i+j)//2
            if matrix[mid][col_max] == target:
                return True
            elif matrix[mid][col_max] < target:
                i = mid+1
            else:
                j = mid
        res = binary_search(matrix[j] , 0 , len(matrix[row])-1 , target )
        
        return res
        