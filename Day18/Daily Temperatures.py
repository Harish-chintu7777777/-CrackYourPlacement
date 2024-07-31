class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stk = []
        res = [0]
        n = len(t)
        for i in range(n-1,-1,-1):
            if not stk:
                stk.append(i)
            elif stk and t[stk[-1]] > t[i]:
                res.append(stk[-1] - i)
                stk.append(i)
            elif stk and t[stk[-1]] <= t[i]:
                while(stk and t[stk[-1]] <= t[i]):
                    stk.pop()
                if stk:
                    res.append(stk[-1] - i)
                else:
                    res.append(0)
                stk.append(i)
            else:
                stk.append(i)
        return res[::-1]
                
        
