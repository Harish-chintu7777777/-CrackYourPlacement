class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        hash_map = [0] * len(nums)
        def backtrack(nums, n, output):
            if len(output) == n:
                result.append(tuple(output[:]))
                return

            for i in range(n):
                if hash_map[i] == 0:
                    hash_map[i] = 1
                    output.append(nums[i])
                    backtrack(nums, n,output)
                    output.pop()
                    hash_map[i] = 0


        backtrack(nums, len(nums), [])
        return sorted(set(result))


        
