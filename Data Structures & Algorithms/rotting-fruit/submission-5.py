class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        input: 2d grid
        output: minutes

        edge: cycle, empty, just one

        plan:
        intiailise a set
        initialise a queue with all rotten fruits and set
        while there's something in the queue
        loop through queue
        pop from queue and add adj fruits if not in set, if it's not empty and add them after
        increment minutes after loop (new level)
        
        return minutes
        '''
        from collections import deque
        
        rows, cols = len(grid), len(grid[0])

        # if rows == 1 and cols == 1 and grid[0][0] != 1:
        #     return 0

        q = deque()
        visited = set()
        minutes = -1


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    visited.add((row,col))
                    q.append((row, col)) #not sure


        while q:

            for _ in range(len(q)):
                row, col = q.popleft()
                directions = [(1,0), (0,1), (0, -1), (-1, 0)]
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r in range(0, rows) and \
                        c in range(0, cols) and \
                        (r,c) not in visited and \
                        grid[r][c] != 0:
                        grid[r][c] = 2
                        q.append((r, c))
                        visited.add((r, c))

            minutes += 1
        #is there more fresh fruit?

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

        return minutes if minutes != -1 else 0


        '''
        [[1,0,1],
         [0,2,0],
         [1,0,1]]
        '''

        

        