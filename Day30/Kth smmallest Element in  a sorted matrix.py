class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        heap = []
        n=len(mat)
        for i in range(n):
            heapq.heappush(heap, (mat[i][0], i, 0))
        
        while k > 0:
            num, i, j = heapq.heappop(heap)
            j += 1
            k -= 1
            if j == n:
                continue
            
            heapq.heappush(heap, (mat[i][j], i, j))
        
        return num
