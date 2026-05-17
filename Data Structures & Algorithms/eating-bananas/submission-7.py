class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        input: arr of nums, h: int
        output: min num of hours

        edge: h < len(piles)

        understand:
        min num of hours == len(piles), k = maxNum
        range(min - max) of arr

        [1, 24, 4, 94, 45, 23, 3], h = 8
        start from max going down until h>8

        h = math.ceil(piles[i] / k)

        plan:
        get max of piles
        initialise k at maxNum
        loop backwards from maxNum
        calculate h for curr k
        if calch becomes greater than h, stop and return curr k
        if not update k

        '''
        maxNum = max(piles)
        l, r = 1, maxNum


        while l <= r:
            mid = (l + r) // 2
            currH = 0
            for num in piles:
                currH += math.ceil(num/mid)

            if currH <= h:
                r = mid - 1
            else:
                l = mid + 1
            
        
        return l

        '''
        1 -> 25
        13
        '''



        # for i in range(1, maxNum + 1):
        #     currH = 0
        #     for num in piles:
        #         currH += math.ceil(num/i)
        
        #     if currH <= h:
        #         return i


        '''
        [1, 4, 3, 2], h = 9

        maxNum = 4
        k = 4
        i: 2 -> -1
        currH = 1 + 2 + 1 + 1 = 5
        currH = 6
        k = 2
        i : 1
        currH = 10
        return 2
        runtime: 
        

        '''










        