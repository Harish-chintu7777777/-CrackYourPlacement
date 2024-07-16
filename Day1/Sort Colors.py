class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        zero,one,two = 0,0,0
        for i in nums:
            if i == 0:
                zero += 1
            elif i == 1:
                one += 1
            else:
                two += 1
        for i in range(n):
            if zero:
                nums[i] = 0
                zero -= 1
                continue
            elif one:
                nums[i] = 1
                one -= 1
                continue
            else:
                two -= 1
                nums[i] = 2
                continue
        return nums
