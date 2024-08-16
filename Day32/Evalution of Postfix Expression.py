class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        stack = []
        operator = ["+","-","*","/","%"]
        
        for item in S:
            if item not in operator:
                stack.append((item))
            else:
                first = int(stack.pop())
                second = int(stack.pop())
            
                if(item == "+"):
                    stack.append(second + first)
                if(item == "-"):
                    stack.append(second - first)
                if(item == "*"):
                    stack.append(second * first)
                if(item == "/"):
                    stack.append(second / first)
                if(item == "%"):
                    stack.append(second % first)
        return stack[-1]
            
