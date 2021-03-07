def longest_non_repeating_sequence(array):
    last_seen_idx_map = {}
    l_idx = r_idx = res = 0
    while l_idx < len(array) and r_idx < len(array):
        item = array[r_idx]
        if item in last_seen_idx_map:
            l_idx = max(l_idx, last_seen_idx_map[item]+1 )
        res = max(res, (r_idx - l_idx+1))
        last_seen_idx_map[item] = r_idx
        r_idx += 1
    return res

print(longest_non_repeating_sequence(['a', 'b', 'a', 'a', 'c', 'a', 'd']))