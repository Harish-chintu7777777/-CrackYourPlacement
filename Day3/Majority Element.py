class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = nums[0]
        c = 1
        for i in nums[1:]:
            if i == maj:
                c += 1
            else:
                c -= 1
                if c == 0:
                    maj = i
                    c = 1
        return maj
