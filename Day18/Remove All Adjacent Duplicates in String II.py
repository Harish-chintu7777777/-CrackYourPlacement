class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk=[['*',0]]
        for i in s:
            if stk[-1][0]==i:
                stk[-1][1]+=1
                if stk[-1][1]==k:
                    stk.pop()
            else:
                stk.append([i,1])
        x=""
        for l,m in stk:
            x+=m*l
        return x

       
