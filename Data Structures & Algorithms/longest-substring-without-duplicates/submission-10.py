class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        s_dict = {}
        maxA = 0
        l = 0
        r =0

        if len(s) == 1:
            return 1

        for r in range(len(s)):

            if s[r] in s_dict and s_dict[s[r]] >= l:
                maxA = max(maxA, r - l)
                l = s_dict[s[r]] + 1
                s_dict[s[r]] = r
            else:
                s_dict[s[r]] = r
                maxA = max(maxA, r - l + 1)
        
        maxA = max(maxA, r - l)

        return maxA