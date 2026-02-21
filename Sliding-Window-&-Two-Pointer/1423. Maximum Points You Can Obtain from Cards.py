class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = 0
        max_sum = 0
        n = len(cardPoints)

        # Initialize lsum as the sum of the first k elements
        for i in range(k):
            lsum += cardPoints[i]
        max_sum = lsum

        rsum = 0
        rindex = n - 1
        # Now, we take i elements from the right and (k - i) from the left
        for i in range(1, k + 1):
            lsum -= cardPoints[k - i]
            rsum += cardPoints[rindex]
            rindex -= 1
            current_sum = lsum + rsum
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum

