class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stk = []
        for i in s:
            if i!=']':
                stk.append(i)
            else:
                curr = ''
                while(stk and stk[-1] != '['):
                    curr = stk.pop() + curr
                stk.pop()

                num = ''
                while(stk and stk[-1].isdigit()):
                    num = stk.pop() + num
                
                stk.append(curr*int(num))
        return "".join(stk)
