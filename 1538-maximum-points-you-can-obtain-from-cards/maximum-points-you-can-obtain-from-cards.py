class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        total = sum(cardPoints)
        n = len(cardPoints)

        window = sum(cardPoints[:n - k])
        min_window = window

        for i in range(n - k, n):
            window += cardPoints[i]
            window -= cardPoints[i - (n - k)]
            min_window = min(min_window, window)

        return total - min_window