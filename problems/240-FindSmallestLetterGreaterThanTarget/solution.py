class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, mid, end = 0, 0, len(letters)-1
        if start==end:
            return letters[start]
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        while start < end:
            mid = start + (end - start)//2
            if letters[mid] == target:
                start = mid + 1
            elif letters[mid] > target:
                end = mid
            else:
                start = mid + 1
        if start == len(letters):
            return letters[0]
        return letters[start]