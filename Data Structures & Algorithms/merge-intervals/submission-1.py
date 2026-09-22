class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        input: intervals[interval[int]]
        output: intervals[inteval[int]]

        edge: empty

        plan:
        sort by first, if they equal sort by second asc
        use stack
        compare second value of last operation with first of new operation
        if first <= sec then they overlap
        pop then insert [old, new]

        [1,5][2, 6] = [1, 6]
        [1, 4][1, 5] = [1, 5]
        [1, 4][2, 3] = 
        '''

        stack = []

        #sort
        intervals.sort()

        for interval in intervals:
            start, end = interval
            
            if stack:
                prevS, prevE = stack[-1]
                if start <= prevE: #overlap
                    stack.pop()
                    stack.append([prevS, max(end, prevE)])
                else:
                    stack.append(interval)
            else:
                stack.append(interval)

        return stack


        '''
        [[1,3],[1,5],[6,7]]
        stack = []
        start, end = 1, 3
        stack = [[1, 3]]
        start, end = 1, 5
        prevS, prevE = 1, 3
        yes => pop
        stack = [[1, 5], [6, 7]]
        '''
