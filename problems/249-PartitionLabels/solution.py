class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_idx_map = {}
        res = []
        for idx, char in enumerate(s):
            end_idx_map[char] = idx
        
        cur_end = 0
        part_len = 0
        for idx, char in enumerate(s):
            cur_end = max(cur_end, end_idx_map[char])
            part_len += 1
            if cur_end == idx:
                res.append(part_len)
                cur_end = idx
                part_len = 0
        return res