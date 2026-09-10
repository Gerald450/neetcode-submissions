from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        input: s:str
        output: arr[int]

        edge: empty

        plan:
        use a Counter to get freqs
        use two pointers, l points to start, r points to finish
        keep incrementing r until freq of s[l] == 0
        after that increment l and do the same until end of s
        if l == r means we done, get length and append to otp
        '''

        freqs = Counter(s)
        l, r = 0, 0
        otp = []
        start = 0
        while r < len(s):

            while freqs[s[l]] != 0:
                freqs[s[r]] -= 1
                r += 1
            l += 1
            if l == r:
                otp.append(l - start)
                start = l

        if r == len(s) and r - start != 0:
            otp.append(r - start)

        return otp
        '''
         "abcabc"
            ^ ^
         {
            a:2 - 1 = 1 - 1 = 0
            b:2 - 1 = 1 - 1 = 0
            c:2 - 1 = 1
         }



        "xyxxyzbzbbisl"
                   ^
         {
         x : 3 - 1 = 2 - 1 = 1 - 1 = 0
         y : 2 - 1 = 1 - 1 = 0
         z : 2 - 1 = 1 - 1 = 0
         b : 3 - 1 = 2 - 1 = 1 - 1 = 0
         i : 1
         s : 1
         l : 1
         }
         r = 0, l = 0
         
        Time: O(n)
         space: O(k)

        '''


        