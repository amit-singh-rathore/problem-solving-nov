def combinationSum(candidates, target):
    dp_uc = defaultdict(set)
    dp_uc[0].add(tuple())
    for partial_sum in range(1, target+1):
        for c in candidates:
            if partial_sum-c>=0:
                for prev_comb in dp_uc[partial_sum-c]:
                    dp_uc[partial_sum].add(tuple(sorted([c] + list(prev_comb))))
    return list(dp_uc[target])