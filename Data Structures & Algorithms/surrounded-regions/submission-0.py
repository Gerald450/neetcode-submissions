class Solution:
    def solve(self, board: List[List[str]]) -> None: 
        '''
        input: grid
        output: grid

        edge:o on edge, no os, empty grid, grid len is 1

        plan:
        capture unsurrounded regions and label them
        change os to xs
        unlabel unsarrounded regions

        '''


        rows, cols = len(board), len(board[0])

        def dfs(row, col):
            if (row < 0 or row >= rows) or (col < 0 or col >= cols) or board[row][col] != "O":
                return
            
            board[row][col] = 'T'

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            


        #capture unsorrounded
        for row in range(rows):
            for col in range(cols):
                if row in [0, rows - 1] or col in [0, cols - 1] and board[row][col] == "O":
                    dfs(row, col)

        #change os to xs
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
        
        #uncapture
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'T':
                    board[row][col] = 'O'

        

        