class Solution:
    def __init__(self):
        self.st = None
        self.length = 0
        self.dp  = None
    def solve(self,idx,A):
        if idx>=self.length:
            return True
        if self.dp[idx]!=-1:
            return self.dp[idx]
        if A in self.st:
            return True
        for i in range(1,self.length+1):
            temp = A[idx:idx+i]
            if temp in self.st and self.solve(idx+i,A):
                self.dp[idx]=1
                return True
        self.dp[idx]=0
        return False
    def wordBreak(self, A, B):
        self.st = set()
        self.length = len(A)
        self.dp = [-1]*(self.length+1)
        for word in B:
            self.st.add(word)
        
        return self.solve(0,A)
