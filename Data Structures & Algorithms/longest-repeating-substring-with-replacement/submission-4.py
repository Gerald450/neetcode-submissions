from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        s_dict = Counter()
        res = 0
        l =0

        for r in range(len(s)):

            s_dict[s[r]] = 1 + s_dict.get(s[r], 0)

            if (r - l + 1) - max(s_dict.values()) > k:
                s_dict[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        return res

        