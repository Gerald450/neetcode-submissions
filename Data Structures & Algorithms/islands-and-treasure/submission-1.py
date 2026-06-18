class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        input: grid
        output: grid with updated cells

        edge: no path, hit -1, empty grid

        plan:
        treverse through grid, if value is equal to INF, call bfs, replace it with minDistance
        bfs(row, col, count) {
           add (row, col, count) to queue
           while queue is not empty:
            pop from it and get the count
            if that value zero then update the minDistance
            and add the neighbors of pop if they not out of bounds, in visited and -1
        }
        ''' 
        from collections import deque
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        
      

        def bfs(row, col):
            count = 0
            minDistance = INF
            visited = set()
            q = deque([(row, col, count)])
            visited.add((row, col))

            while q:
                row, col, count = q.popleft()
                if grid[row][col] == 0:
                    minDistance = min(minDistance, count)
                
                directions = [(1,0), (0, 1), (-1, 0), (0, -1)]

                for dr in directions:
                    rr, cc = dr
                    r, c = row + rr, col + cc
                    if (r in range(0, rows) and c in range(0, cols)) and \
                        (r, c) not in visited and \
                        grid[r][c] != -1:
                        q.append((r, c, count + 1))
                        visited.add((r, c))

            return minDistance




        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == INF:
                    grid[row][col] = bfs(row, col)


        '''
        [
        [2147483647,        -1,         0, 2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,        -1,2147483647,-1],
        [0,                 -1,2147483647, 2147483647]
        ]

        rows = 4
        cols = 4


        '''











        