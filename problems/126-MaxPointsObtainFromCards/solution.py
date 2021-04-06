class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        head = sum(cardPoints[:k])
        tail = 0
        cur_max = head + tail
        for i in range(k-1,-1, -1):
            head -= cardPoints[i]
            tail += cardPoints[i-k]
            cur_max = max(cur_max, head + tail)
        return cur_max