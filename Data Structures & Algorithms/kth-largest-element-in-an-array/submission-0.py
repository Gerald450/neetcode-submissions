class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        negatedNums = [-num for num in nums]

        heapq.heapify(negatedNums)

        for _ in range(k):
            res = heapq.heappop(negatedNums)

        return res * -1

        