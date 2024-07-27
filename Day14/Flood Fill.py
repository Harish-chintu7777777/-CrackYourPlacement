class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
    
        m = len(image)
        n = len(image[0])
        vis = set()
        initt = image[sr][sc]
    
        def bfs(row, col):
            q = []
            q.append((row, col))
            vis.add((row, col))
            while q:
                r, c = q.pop(0)
                for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nrow = r + i
                    ncol = c + j
                    if 0 <= nrow < m and 0 <= ncol < n and (nrow, ncol) not in vis and image[nrow][ncol] == initt:
                        image[nrow][ncol] = color
                        q.append((nrow, ncol))
                        vis.add((nrow, ncol))
    
        if image[sr][sc] != color:
            image[sr][sc] = color
            bfs(sr, sc)
    
        return image

        
