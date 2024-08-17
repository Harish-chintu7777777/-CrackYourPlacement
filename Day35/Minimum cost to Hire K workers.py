class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted((w/q, w, q) for q, w in zip(quality, wage))
        heap, res, sumq = [], float('inf'), 0

        for r, w, q in workers:
            heapq.heappush(heap, -q)
            sumq += q
            if len(heap) > K:
                sumq += heapq.heappop(heap)
            if len(heap) == K:
                res = min(sumq * r, res)
        return res
        
