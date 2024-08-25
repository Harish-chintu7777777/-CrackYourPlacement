class Solution:
    
    def maxCoins(self, nums: List[int]) -> int:
    
        def recurse(low, high):

            if low == high:
                return nums[low - 1] * nums[low] * nums[low + 1]
            
            if dp[low][high] != -1:
                return dp[low][high]
            
            ans = 0
            for mid in range(low, high + 1):
                left_ans = recurse(low, mid - 1)
                right_ans = recurse(mid + 1, high)

                cur_ans = nums[low - 1] * nums[mid] * nums[high + 1]
                ans = max(ans, left_ans + right_ans + cur_ans)

            dp[low][high] = ans
            return ans

        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[-1] * n for i in range(n)]
        return recurse(1, n - 2)
