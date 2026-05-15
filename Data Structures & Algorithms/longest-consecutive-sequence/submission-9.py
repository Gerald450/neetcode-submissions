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

        optimization:
        find start of seq, and only start from there
        '''

      
        maxSequence = 0
        hashset = set(nums)
        seq = 0

        for num in nums: #O(n)
            
            if num - 1 not in hashset:
                curr = num
                seq = 1

                while curr + 1 in hashset:
                    seq += 1
                    curr += 1
            maxSequence = max(maxSequence, seq)


        return maxSequence
    

        '''
        hashset = {0,3,2,5,4,6,1,1}
        
        runtime O(n^2) space O(n)
        
        '''








        