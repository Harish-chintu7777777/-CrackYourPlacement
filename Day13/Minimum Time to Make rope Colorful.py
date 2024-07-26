class Solution:
    def minCost(self, cs: str, nt: List[int]) -> int:
        
        i,j = 0,1
        cnt,s,maxi = 0,nt[0],nt[0]
        n = len(cs)
        while(i<j and  j<n):
            if cs[i] == cs[j]:
                s += nt[j]
                maxi = max(maxi,nt[j])
                j += 1
            else:
                cnt += s-maxi
                i = j
                j += 1
                s = nt[i]
                maxi = nt[i]
        
        cnt += s-maxi
        return cnt
