class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        input: two arr of sorted nums
        output: median of two

        edge: one is empty, or both

        plan:
        create two pointers
        compare pointers at each pass
        create a new combined sorted arr
        '''

        newArr = []
        l1, l2 = 0, 0

        while l1 < len(nums1) and l2 < len(nums2):

            if nums1[l1] <= nums2[l2]:
                newArr.append(nums1[l1])
                l1 += 1
            else:
                newArr.append(nums2[l2])
                l2 += 1



        newArr.extend(nums1[l1:])
        newArr.extend(nums2[l2:])
        length = len(newArr)

        if length % 2:
            med = (length - 1) // 2
            return newArr[med]
        else:
            med = length // 2
            return (newArr[med - 1] + newArr[med]) / 2
        

