class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def insertionSort(array):
            for i in range(1, len(array)):
                key = array[i]
                j = i-1
                while array[j] > key and j >= 0:
                    array[j+1] = array[j]
                    j -= 1
                array[j+1] = key
            return array

        def merge(arr1, arr2):
            ptr1 = 0
            ptr2 = 0
            res = []

            while ptr1 < len(arr1) and ptr2 < len(arr2):
                if arr1[ptr1] < arr2[ptr2]:
                    res.append(arr1[ptr1])
                    ptr1 += 1
                elif arr1[ptr1] > arr2[ptr2]:
                    res.append(arr2[ptr2])
                    ptr2 += 1
                else:
                    res.append(arr1[ptr1])
                    res.append(arr2[ptr2])
                    ptr1 += 1
                    ptr2 += 1

            while ptr1 < len(arr1):
                res.append(arr1[ptr1])
                ptr1 += 1

            while ptr2 < len(arr2):
                res.append(arr2[ptr2])
                ptr2 += 1

            return res

        def timSort(array, threshold):
            for idx in range(0, len(array), threshold):
                array[idx : idx + threshold] = insertionSort(array[idx : idx + threshold])
            interval = threshold
            while interval < len(array):
                for idx in range(0, len(array), 2 * interval):
                    array[idx : idx + 2 * interval] = merge(array[idx : idx + interval], array[idx + interval: idx + 2 * interval])
                interval = interval * 2
        
        timSort(nums, 32)
        return nums
