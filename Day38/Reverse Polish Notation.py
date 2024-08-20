class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk = []
        for i in tokens:
            if i not in '+-*/':
                stk.append(i)
            else:
                if len(stk) >= 2:
                    x=stk.pop()
                    y=stk.pop()
                    
                    if i=="+":
                        stk.append(str(int(x)+int(y)))
                    elif i=="-":
                        stk.append(str(int(y)-int(x)))
                    elif i=="*":
                        stk.append(str(int(x)*int(y)))
                    else:
                        stk.append(str(int(int(y) / int(x))))
                else:
                    stk.append(i)
        return int(stk[-1])
