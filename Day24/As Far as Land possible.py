class Solution:
    def maxDistance(self, grid):
        ROW, COL = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = []
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))

        if not queue or len(queue) == ROW * COL:
            return -1

        while queue:
            x, y, dist = queue.pop(0)
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < ROW and 0 <= new_y < COL and grid[new_x][new_y] == 0:
                    grid[new_x][new_y] = 1
                    queue.append((new_x, new_y, dist + 1))

        return dist
