class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if not tree:
            return 0
        freq_map = {}
        left, cur_max = 0, 0
        for right, item in enumerate(tree):
            freq_map[item] = freq_map.get(item, 0) + 1
            while len(freq_map) > 2:
                amount = freq_map.get(tree[left]) - 1
                if amount == 0: 
                    del freq_map[tree[left]]
                else:
                    freq_map[tree[left]] = amount
                left += 1
            window = right - left + 1
            cur_max = window if window > cur_max else cur_max
        return cur_max;