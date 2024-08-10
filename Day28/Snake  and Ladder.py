Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> class Solution:
...     def snakesAndLadders(self, board: List[List[int]]) -> int:
...         
...         n = len(board)
...         board.reverse()
...         def intToPos(square):
...             r = (square - 1) // n
...             c = (square - 1) % n
... 
...             if r%2:
...                 c = n - c - 1
...             return [r, c]
...         q = []
...         q.append([1, 0])
...         vis = set()
...         while(q):
...             square, moves = q.pop(0)
... 
...             for i in range(1, 7):
...                 nextSq = square + i
...                 r, c = intToPos(nextSq)
...                 if board[r][c] != -1:
...                     nextSq = board[r][c]
...                 if nextSq == n*n:
...                     return moves + 1
...                 if nextSq not in vis:
...                     vis.add(nextSq)
...                     q.append([nextSq, moves+1])
...         return -1
... 
... 
