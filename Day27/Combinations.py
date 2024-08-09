class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def f(ind, temp, size,k, n, l, res):
            
            if size<=0:
                if len(temp)==k:
                    res.append(temp[:])
                return
            if ind>=len(l):
                return

            temp.append(l[ind])
            f(ind + 1, temp, size-1,k, n, l, res)
            temp.pop()
            f(ind + 1, temp, size,k, n, l, res)



        l = [i for i in range(1, n + 1)]
        temp = []
        res = []
        f(0, temp, k,k, n, l, res)
        return res

        


