class Solution:
    def leastInterval(self, tasks: List[str], k: int) -> int:                                                   
        n = len(tasks)
        d = Counter(tasks)
        heap = [-j for i,j in d.items()]
        heapq.heapify(heap)
        time = 0
        q = []
        while(heap or q):
            
            time += 1
            if heap:
                cnt = 1+heapq.heappop(heap)
                if cnt:
                    q.append([cnt,time+k])
            if q:
                if q[0][1] == time:
                    heapq.heappush(heap,q.pop(0)[0])
        return time

            
