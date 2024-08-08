class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=[]
        r=[]
        d=Counter(nums)
        heapq.heapify(r)
        for i,j in d.items():
            heapq.heappush(r,[-j,i])
        while(k>0):
            l.append(heapq.heappop(r)[1])
            k-=1
        return l
            
        
