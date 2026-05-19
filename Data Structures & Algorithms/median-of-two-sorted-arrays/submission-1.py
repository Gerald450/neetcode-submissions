class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        input: two num arrays
        ouput: int median of both

        edge: if one is empty, or both, not same size

        plan:
        do binary on shorter arr
        find mid and use that to find remainder of left partition in second array
        check if the partitions are correct by comparing the values
        if not move pointers in shorter array to fix it
        '''

        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2

        '''
        l, r = 0, 1
        half = 2 + 1 = 3//2 = 1
        midA = 1 // 2 = 0
        midB = 1 - 0 - 2 = -1
        '''

        while True:
            midA = (l + r) // 2
            midB = half - midA - 2

            Aright= A[midA + 1] if (midA + 1) < len(A) else float('infinity')
            Aleft = A[midA] if midA >= 0 else float('-infinity')
            Bright = B[midB + 1] if (midB + 1) < len(B) else float('infinity')
            Bleft = B[midB] if midB >= 0 else float('-infinity')

            #correct pratition
            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = midA - 1
            else:
                l = midA + 1


        '''
        [1, 2], [3]
        l = 0, r = 0 
        total = 3
        half = 1
        midA = 0
        midB = 1 - 0 - 2 = -1
        Aright = inf
        Aleft = 3
        Bright = 1
        Bleft = -inf

        r = 0 - 1 = -1
        midA = 0
        midB = 1 - 0 - 2 = -1

        Aright = 3
        Aleft = -inf
        Bright = 2
        Bleft = 1

        2


        runtime O(log(A))
        space O(1)

        '''









        '''
        [1, 3], [2, 4]

        l = 0, r = 1
        total = 4
        half = 2
        midA = 0
        midB = 2 - 2 = 0
        Aright = A[1] = 3
        Aleft = 1
        Bright = 4
        Bleft = 2

        2 + 3 / 2 = 2.5

        '''



















        