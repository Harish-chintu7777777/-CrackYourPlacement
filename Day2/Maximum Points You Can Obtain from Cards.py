class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        lsum = sum(cardPoints[:k])
        maxi = lsum
        rsum = 0
        r_ind = n-1
        for i in range(k-1,-1,-1):
            lsum -= cardPoints[i]
            rsum += cardPoints[r_ind]
            r_ind -= 1
            maxi = max(maxi,lsum + rsum)
        return maxi

