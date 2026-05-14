class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        l = 0 
        maxl = 0

        for r in range(len(s)):
            dic[s[r]] = 1 + dic.get( s[r], 0 )
            
            if (r-l+1) - max(dic.values()) > k:
                dic[s[l]] -= 1
                l += 1
            maxl = max(maxl, r - l + 1)
            
        return maxl