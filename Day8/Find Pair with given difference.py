from typing import List
class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        # code here
        d = {}
        for i in arr:
            if i-x in d or i+x in d:
                return 1
            else:
                d[i] = 1
        return -1
        
