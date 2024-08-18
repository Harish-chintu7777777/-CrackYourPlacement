class BIT:
    def __init__(self,nums):
        self.bi_tree = [0]*(len(nums)+1)
        self.n = len(nums)
        for i in range(self.n):
            self.update(i+1,nums[i])
    def update(self,ind,val):
        while(ind<=self.n):
            self.bi_tree[ind] += val
            ind += ind & (-ind)
    def get_sum(self,ind):
        pre = 0
        while(ind>0):
            pre += self.bi_tree[ind]
            ind -= ind & (-ind)
        return pre

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bi_tree = BIT(nums)

    def update(self, index: int, val: int) -> None:
        
        self.bi_tree.update(index+1,val - self.nums[index])
        self.nums[index] = val
        
    def sumRange(self, left: int, right: int) -> int:
        return self.bi_tree.get_sum(right+1)-self.bi_tree.get_sum(left)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
