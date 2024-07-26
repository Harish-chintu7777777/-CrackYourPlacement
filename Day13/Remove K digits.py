class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stk = []
        for i in num:
            while(k and stk and stk[-1] > i):
                k -= 1
                stk.pop()
            stk.append(i)
        while(k):
            k -= 1
            stk.pop()
        stk = "".join(stk).lstrip("0")
        return stk if stk else '0'
