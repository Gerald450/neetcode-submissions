class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        input: arr of nums, int: k
        output: array of top k most freq elements
        edge cases: empty, same freq, k > available nums

        plan:
        use counter to get freq
        make a tuple from counter(negate the freq)(-freq, num)
        use maxheap by freq
        pop k times

        optimization:
        bucket sort
        '''

        from collections import Counter
        import heapq

        hashmap = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in hashmap.items():
            bucket[value].append(key)

        otp = []
        for i in range(len(nums), -1, -1):
            if bucket[i]:
                for j in range(len(bucket[i])):
                    otp.append(bucket[i][j])
            if len(otp) == k:
                return otp

        return otp

        '''
        hashmap = {7:2}
        bucket = [[], [], [7]]


        '''


        '''
        nums = {2, 3, 1, 2, 3, 2, 4, 4, 4, 4}, k = 2
        hashmap = {2: 3, 3: 2, 1: 1, 4: 4}
        freqArr = [(-3, 2), (-2, 3), (-1, 1), (-4, 4)]
        time O(nlogn) space O(n)
        '''








        