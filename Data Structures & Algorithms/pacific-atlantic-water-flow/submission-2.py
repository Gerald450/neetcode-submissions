class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        input: grid
        output: list of list of coordinates

        edge: grid is empty, no flow

        plan:
        put all pacific reach cells in a queue and set
        put all atlantic reaching cells in a queue and set
        bfs and all cells that pacific can reach add then to pacific set
        same as atlantic
        '''

        from collections import deque

        pacific_q = deque()
        atlantic_q = deque()
        pacific_set = set()
        atlantic_set = set()

        rows, cols = len(heights), len(heights[0])

        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    pacific_q.append((row, col))
                    pacific_set.add((row,col))
                if row == rows - 1 or col == cols - 1:
                    atlantic_q.append((row, col))
                    atlantic_set.add((row, col))
        
        pacific_list = list(pacific_set)
        atlantic_list = list(atlantic_set)

    
        def bfs(q, hashmap):
            visited = set()
            while q:
                row, col = q.popleft()
                visited.add((row, col))
                directions = [(1,0), (0,1), (0,-1), (-1,0)]
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r in range(0, rows) and \
                        c in range(0, cols) and \
                        heights[r][c] >= heights[row][col] and \
                        (r, c) not in visited:
                        q.append((r,c))
                        hashmap.add((r, c))

            return hashmap


        for row, col in pacific_list:
            pacific_set.update(bfs(pacific_q, pacific_set))

       

        for row, col in atlantic_list:
            atlantic_set.update(bfs(atlantic_q, atlantic_set))


        
        
        result = atlantic_set.intersection(pacific_set)

        return list(result)








        