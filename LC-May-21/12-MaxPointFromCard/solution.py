class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = sum(cardPoints[:k])
        right_sum = 0
        max_points = left_sum + right_sum
        for idx in range(k-1,-1, -1):
            left_sum -= cardPoints[idx]
            right_sum += cardPoints[idx-k]
            max_points = max(max_points, left_sum + right_sum)
        return max_points