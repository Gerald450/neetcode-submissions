class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def bfs(i):

            if i >= len(nums):
                res.append(subset.copy())
                return
            

            #choose to take current:
            subset.append(nums[i])
            bfs(i+1)

            #choose not to:
            subset.pop()
            bfs(i+1)
        
        bfs(0)
        return res
        

        