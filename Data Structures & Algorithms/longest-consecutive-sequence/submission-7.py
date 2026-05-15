class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        input: array of nums
        output: int: len of longest sequence

        edge cases: no sequence, empty arr, duplicates

        plan:
        loop through arr
        figure out the start of sequence
        use a set for O(1) lookup, so make a set of nums
        while there is a number less than one the curr in set increment maxSequence count
        change curr to the less than one num
        return maxSequence
        '''

        maxSequence = 0
        hashset = set(nums)

        for num in nums:
            curr = num - 1
            sequence = 1
            while curr in hashset:
                sequence += 1
                curr -= 1
            maxSequence = max(maxSequence, sequence)

        return maxSequence

        '''
        hashset = {0,3,2,5,4,6,1,1}
        
        
        
        '''








        