class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        
        @lru_cache(None)
        def dp(l, r, count = 0):
            if l > r: return 0
            count += 1 
            while l+1 <= r and boxes[l+1] == boxes[l]:
                l+=1
                count+=1 
 
            ans = (count)**2 + dp(l+1, r, 0)
            
            for next_i in range(l+1, r+1):
                if boxes[next_i]==boxes[l]:
                    next_occurence_of_boxesl = dp(next_i, r, count) 
                    in_between_deletion = dp(l+1, next_i - 1, 0)
                    ans = max(ans, next_occurence_of_boxesl + in_between_deletion)
            return ans
        return dp(0, len(boxes)-1)
