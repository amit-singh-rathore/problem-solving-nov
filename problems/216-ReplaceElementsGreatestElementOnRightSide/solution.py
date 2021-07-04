class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        cur_max = arr[n-1]
        arr[n-1] = -1
        
        for i in range(n-2, -1, -1):
            temp = cur_max
            if arr[i] > cur_max:
                cur_max = arr[i]
            arr[i] = temp
        return arr
                
        