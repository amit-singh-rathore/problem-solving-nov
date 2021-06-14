class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        increasing = decreasing = 0
        for i in range(len(arr)-1):
            if decreasing == 0 and arr[i] < arr[i+1]:
                increasing += 1
            elif increasing > 0 and arr[i] > arr[i+1]:
                decreasing += 1
        return increasing > 0 and decreasing > 0 and (increasing + decreasing == len(arr) - 1)


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        i,j = 0,1
        
        while j < len(arr):
            if arr[j] > arr[i]:
                i += 1
                j += 1
            elif arr[j] == arr[i]:
                return False
            else:
                break
                
        if j == len(arr) and arr[j - 1] > arr[i - 1]:
            return False
        
        if j == 1 and i == 0 and arr[j] < arr[i]:
            return False
        
        while j < len(arr):
            if arr[j] < arr[i]:
                i += 1
                j += 1
            else:
                return False
        return True
            
            