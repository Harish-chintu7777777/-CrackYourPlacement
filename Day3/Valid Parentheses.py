class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        d = {")":"(","]":"[","}":"{"}
        for i in s:
            if not stk:
                stk.append(i)
            elif stk and i in d and stk[-1] == d[i]:
                stk.pop()
            else:
                stk.append(i)
        return not stk
        
