class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        
        idx_map = {}
        for idx, value in enumerate(nums):
            if value in idx_map and (idx - idx_map[value]) <= k:
                return True
            else:
                idx_map[value] = idx
        return False