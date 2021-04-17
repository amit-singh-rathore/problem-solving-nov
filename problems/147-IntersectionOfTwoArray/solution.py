class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        l1 = len(nums1)
        l2 = len(nums2)
        i, j = 0, 0
        res = []
        while i<l1 and j<l2:
        
            if nums1[i]>nums2[j]:
                j += 1
            elif nums1[i]<nums2[j]:
                i += 1
            else:
                res.append(nums1[i]);
                i += 1
                j += 1

        return res
