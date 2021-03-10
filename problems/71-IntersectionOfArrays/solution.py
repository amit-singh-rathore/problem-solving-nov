def intersection(nums1, nums2):
    if len(nums1)>len(nums2):
        n1 = set(nums1)
        res = [x for x in nums2 if x in n1]
    else:
        n1 = set(nums2)
        res =  [x for x in nums1 if x in n1]
    return list(set(res))
        