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
        '''

        from collections import Counter
        import heapq

        hashmap = Counter(nums)
        freqArr = []

        for key, value in hashmap.items():
            freqArr.append((-value, key))

        heapq.heapify(freqArr)
        otp = []
        for _ in range(k):
            freq, num = heapq.heappop(freqArr)
            otp.append(num)

        return otp


        '''
        nums = {2, 3, 1, 2, 3, 2, 4, 4, 4, 4}, k = 2
        hashmap = {2: 3, 3: 2, 1: 1, 4: 4}
        freqArr = [(-3, 2), (-2, 3), (-1, 1), (-4, 4)]





        '''








        