class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ins_idx = []
        for idx, item in enumerate(arr):
            if item == 0:
                ins_idx.append(idx)
        
        for inc, idx in enumerate(ins_idx, 1):
            arr.insert(inc+idx, 0)
            arr.pop()
   
# Optimized solution   
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        n = len(arr)
        idx_shft = 0

        for i in range(n):
            if i > n - 1 - idx_shft:
                break

            if arr[i] == 0:
                if i == n - 1 - idx_shft:
                    arr[n - 1] = 0
                    n -= 1
                else:
                    idx_shft += 1

        for idx in range(n - 1 - idx_shft, -1, -1):
            if arr[idx] == 0:
                arr[idx + idx_shft] = 0
                idx_shft -= 1
                arr[idx + idx_shft] = 0
            else:
                arr[idx + idx_shft] = arr[idx]
            
                
                