class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        island = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        seen = set()


        def bfs(r, c):
            q = deque([(r,c)])
            seen.add((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    rr, cc = row + dr, col + dc
                    if (rr in range(rows)
                        and cc in range(cols)
                        and (rr, cc) not in seen
                        and grid[rr][cc] == "1"):

                        q.append((rr, cc))
                        seen.add((rr, cc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    bfs(r, c)
                    island += 1

        return island























        # rows, cols = len(grid), len(grid[0])
        # def dfs(r, c):
        #     if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]) or grid[r][c] == '0':
        #         return 0
        #     grid[r][c] = '0'
        #     dfs(r + 1, c)
        #     dfs(r - 1, c)
        #     dfs(r, c + 1)
        #     dfs(r, c - 1)
        #     return 1
        # count = 0
        # for r in range(rows):
        #     for c in range(cols):
        #         count += dfs(r, c)
        # return count