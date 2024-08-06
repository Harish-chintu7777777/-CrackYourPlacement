class Solution:

    def findCheapestPrice(self, n: int, edges: List[List[int]], src: int, dst: int, k: int) -> int:

        adj={}

        for i in range(n):

            adj[i]=[]

            

        for i in edges:

            adj[i[0]].append([i[1],i[2]])

        

        

        q=[]

        

        dist=[float("inf")]*n

        dist[src]=0

        q.append((0,src,0))

        while(q):

            stops,node,cost=q.pop(0)

            if stops>k:

                continue

            for it in adj[node]:

                adjNode=it[0]

                adjwt=it[1]

                if cost+adjwt<dist[adjNode] and stops<=k:

                    dist[adjNode]=cost+adjwt

                    q.append((stops+1,adjNode,cost+adjwt))

                

        if dist[dst]==float("inf"):

            return -1

        return dist[dst]

        
