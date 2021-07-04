class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for item in arr:
            if item/2 in seen or item * 2 in seen:
                return True
            else:
                seen.add(item)
        return False