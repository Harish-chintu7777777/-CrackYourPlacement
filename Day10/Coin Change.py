class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # def f(ind,amount,dp):
        #     if ind==0:
        #         if amount%coins[0]==0:
        #             return amount//coins[0]
        #         else:
        #             return int(1e9)
        #     if dp[ind][amount]!=-1:
        #         return dp[ind][amount]

        #     not_take=0+f(ind-1,amount,dp)
        #     take=int(1e9)
            
        #     if coins[ind]<=amount:
        #         take=1+f(ind,amount-coins[ind],dp)
        #     dp[ind][amount]=min(take,not_take)
        #     return dp[ind][amount]
      
        # n=len(coins)
        # dp=[[-1]*(amount+1) for j in range(n)]
        # ans = f(n-1,amount,dp)
        # if ans>=int(1e9):
        #     return -1
        def minimumElementsUtil(arr, ind, T, dp):
            if ind == 0:
                if T%arr[0] == 0:
                    return T//arr[0]
                else:
                    return int(1e9)
            if dp[ind][T] != -1:
                return dp[ind][T]
            notTaken = 0 + minimumElementsUtil(arr, ind-1, T, dp)
            taken = int(1e9)
            if arr[ind] <= T:
                taken = 1 + minimumElementsUtil(arr, ind, T-arr[ind], dp)
            dp[ind][T] = min(notTaken, taken)
            return dp[ind][T]


        n = len(coins)
        dp = [[-1 for j in range(amount+1)] for i in range(n)]
        ans = minimumElementsUtil(coins, n-1, amount, dp)
        if ans >= int(1e9):
            return -1
        return ans
