class Solution:
    def countBits(self, n: int) -> List[int]:
        x=[str(bin(i).replace("0b","")).count("1") for i in range(0,n+1)]
        return x
        
