class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        maxA = 0
        seen = set()
        
        def bfs(r, c):
            q = deque([(r, c)])
            seen.add((r,c))
            area = 1

            while q:
                row, col = q.popleft()
        
                for dr, dc in directions:
                    rr, cc = row + dr, col + dc

                    if (rr in range(rows) and
                        cc in range(cols) and
                        grid[rr][cc] == 1 and
                        (rr, cc) not in seen):
                        area += 1
                        q.append((rr, cc))
                        seen.add((rr, cc))
            
            return area

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    maxA = max(maxA, bfs(r, c))
                    

        return maxA
                
        