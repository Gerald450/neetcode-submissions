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
        check if there's still fresh fruit
        
        return minutes
        '''
        from collections import deque
        
        rows, cols = len(grid), len(grid[0])

        q = deque()
        minutes = -1


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col)) #not sure


        while q:

            for _ in range(len(q)):
                row, col = q.popleft()
                directions = [(1,0), (0,1), (0, -1), (-1, 0)]
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r in range(0, rows) and \
                        c in range(0, cols) and \
                        grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r, c))

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


         runtime: O(nm)
         space: O(nm)
        '''

        

        