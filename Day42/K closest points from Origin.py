class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = [[(i[0]**2 + i[1]**2)**(0.5),i] for i in points]
        res.sort()
        res1 = []
        for i in range(k):
            res1.append(res[i][1])
        return res1
