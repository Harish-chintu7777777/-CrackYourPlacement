
class Solution:
    def dfs(self, i, j, idx, length, mat, word, vis, m, n):
        vis.add((i, j))
        if length == 0:
            return True
        for row, col in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            nrow, ncol = i + row, j + col
            if 0 <= nrow < m and 0 <= ncol < n and (nrow, ncol) not in vis and mat[nrow][ncol] == word[idx]:
                if self.dfs(nrow, ncol, idx + 1, length - 1, mat, word, vis, m, n):
                    return True
        vis.remove((i, j))
        return False

    def exist(self, mat: List[List[str]], word: str) -> bool:
        ind = 0
        s = len(word)
        m = len(mat)
        n = len(mat[0])
        vis = set()
        x = False

        for i in range(m):
            for j in range(n):
                if mat[i][j] == word[ind]:
                    x = self.dfs(i, j, ind + 1, s - 1, mat, word, vis, m, n)
                    if x:
                        return True

        return False
