class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def bfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            #include curr
            curr.append(nums[i])
            bfs(i, curr, total + nums[i])

            #don't include it
            curr.pop()
            bfs(i + 1, curr, total)

        bfs(0, [], 0)

        return res
