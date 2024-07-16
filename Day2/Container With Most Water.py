class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        i,j = 0,n-1
        maxi = -1e9
        while(i<j):
            maxi = max(maxi,(j-i)*(min(height[i],height[j])))
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return maxi
