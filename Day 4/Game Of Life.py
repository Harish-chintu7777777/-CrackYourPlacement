
>>> class Solution:
...     def gameOfLife(self, board: List[List[int]]) -> None:
...     
...         m, n = len(board), len(board[0])
...         directions = [(1,0),(0,1),(-1,0),(0,-1), (1,1),(-1,-1),(1,-1), (-1,1)]
...         visited = [["" for _ in range(n)]for _ in range(m)]
...         
...         for r in range(m):
...             for c in range(n):
...                 live = 0
...                 for dr,dc in directions:
...                     if 0 <= r + dr < m and 0 <= c + dc < n and board[r + dr][c + dc] == 1:
...                         live += 1
... 
...                 if board[r][c] == 1:
...                     if live < 2:
...                         visited[r][c] = "X"
...                     elif live == 2 or live == 3:
...                         visited[r][c] = "L"
...                     elif live > 3:
...                         visited[r][c] = "X"
...                 
...                 if board[r][c] == 0:
...                     if live == 3:
...                         visited[r][c] = "L"
...                     else:
...                         visited[r][c] = "X"
...         
...         for i in range(m):
...             
...             for j in range(n):
...                 if visited[i][j] == "X":
...                     board[i][j] = 0
...                 else:
