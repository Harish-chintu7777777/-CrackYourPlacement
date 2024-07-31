class Solution:
    def tour(self,lis, n):
        
        if sum([lis[i][0] for i in range(n)]) < sum([lis[i][1] for i in range(n)]):
            return -1
        else:
            petrol = [lis[i][0] for i in range(n)]
            distance = [lis[i][1] for i in range(n)]
            
            total = 0
            res = 0
            for i in range(n):
                total += petrol[i]-distance[i]
                if total < 0:
                    total = 0
                    res = i+1
            return res
                    
