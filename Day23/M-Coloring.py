
def graphColoring(graph, k,V ):
    def issafe(n,kl,colr):
        for i in range(V):
            if graph[i][n]==1 and colr[i]==kl:
                return False
        return True
    def helper(v,colr,kl):
        if V==v:
            return True
        if kl>k:
            return False
        if issafe(v,kl,colr):
            colr[v]=kl
            if(helper(v+1,colr,1)):
                return True
            colr[v]=-1
        return helper(v,colr,kl+1)

    colr=[-1]*V
    return helper(0,colr,1)
