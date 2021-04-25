class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq_map = Counter(text)
        return int(min(freq_map['b'], freq_map['a'], freq_map['n'], freq_map['l'] // 2, freq_map['o'] // 2))