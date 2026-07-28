class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(x, y):
            q = deque()
            q.append((x, y))

            cnts = 0

            while q:
                x, y = q.popleft()
                if grid[y][x] == "0":
                    continue

                grid[y][x] = "x"
                cnts += 1

                for dx, dy in dirs:
                    nx, ny = dx + x, dy + y
                    if (
                        nx >= 0
                        and nx < len(grid[0])
                        and ny >= 0
                        and ny < len(grid)
                        and grid[ny][nx] == "1"
                    ):
                        q.append((dx + x, dy + y))

            return cnts > 0

        n = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    if bfs(x, y):
                        n += 1

        return n
