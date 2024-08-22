class Solution:

    def minimum(self, arr):
        idx = 0
        m = float('inf')

        for i in range(len(arr)):
            if arr[i] < m:
                m = arr[i]
                idx = i
        return idx

    def maximum(self, arr):
        idx = 0
        m = float('-inf')

        for i in range(len(arr)):
            if arr[i] > m:
                m = arr[i]
                idx = i
        return idx

    def minCashFlow(self, transaction, n):
        netAmount = [0] * n

        for i in range(n):
            for j in range(n):
                netAmount[i] += (transaction[j][i] - transaction[i][j])

        numberOfZero = 0

        for i in range(n):
            if netAmount[i] == 0:
                numberOfZero += 1

        answer = [[0] * n for _ in range(n)]

        while numberOfZero != n:
            minAmountIdx = self.minimum(netAmount)
            maxAmountIdx = self.maximum(netAmount)

            if netAmount[maxAmountIdx] > abs(netAmount[minAmountIdx]):
                answer[minAmountIdx][maxAmountIdx] = abs(
                    netAmount[minAmountIdx])
                netAmount[maxAmountIdx] -= abs(netAmount[minAmountIdx])
                netAmount[minAmountIdx] = 0
            elif netAmount[maxAmountIdx] < abs(netAmount[minAmountIdx]):
                answer[minAmountIdx][maxAmountIdx] = netAmount[maxAmountIdx]
                netAmount[minAmountIdx] += netAmount[maxAmountIdx]
                netAmount[maxAmountIdx] = 0
            else:
                answer[minAmountIdx][maxAmountIdx] = abs(
                    netAmount[minAmountIdx])
                netAmount[maxAmountIdx] = 0
                netAmount[minAmountIdx] = 0
                numberOfZero += 1

            numberOfZero += 1

        return answer
