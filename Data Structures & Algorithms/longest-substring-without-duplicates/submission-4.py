class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        maxR = 0
        l = 0
        r = 0
        if len(s) == 1:
            return 1
        
        while r < len(s):
            
            if s[r] in s_set:
                s_set = set()
                l += 1
                r = l
            else:
                s_set.add(s[r])
                r += 1
            maxR = max(maxR, (r - l))
        return maxR
            