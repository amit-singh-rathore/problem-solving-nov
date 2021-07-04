class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count_freq = [0] * 101
        for ht in heights:
            count_freq[ht] += 1
        idx, res = 0, 0
        for ht, freq in enumerate(count_freq):
            if freq == 0:
                continue
            for _ in range(freq):
                if ht != heights[idx]:
                    res += 1
                idx += 1
        return res