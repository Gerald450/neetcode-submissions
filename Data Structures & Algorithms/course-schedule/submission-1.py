class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        input: numCourses, array of arrays
        output: boolean

        edge: circle

        plan:
        make a hashmap with key num and value array of prerequisites
        loop through in range numCourses
        call dfs on every num, if it returns false quickly return false

        dfs(
            base case: if value is empty, return true
            if num in seen, false

            add to set

            loop through values of passed key
            if dfs returns false return false

            remove from set
            update that key to empty values, for later ones
            return True
        )
        '''

        from collections import defaultdict

        hashmap = defaultdict(list)
        seen = set()

        for pre in prerequisites:
            a, b = pre
            hashmap[a].append(b)
        
        def dfs(num):
            if not hashmap[num]:
                return True
            if num in seen:
                return False
            
            seen.add(num)

            for val in hashmap[num]:
                if not dfs(val):
                    return False
            
            seen.remove(num)
            hashmap[num] = []
            return True


        for num in range(numCourses):
            if not dfs(num):
                return False

        return True


        '''
        hashmap = {
            0:1,
            1:0
        }
        seen = {0}
        false

        v: numCourses
        e: len(prerequisites)
        runtime: O(V + E)
        space: O(V + E)
        '''

        