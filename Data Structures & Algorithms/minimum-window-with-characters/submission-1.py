
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #create to Counters
        #have, need

        if s == '':
            return ''

        sd = Counter()
        td = Counter(t)

        have, need = 0, len(td)

        res, reslen = [-1,-1], float('infinity')
        
        l = 0

        for r in range(len(s)):

            sd[s[r]] = 1 + sd.get(s[r], 0)

            if s[r] in td and td[s[r]] == sd[s[r]]:
                have += 1

            while have == need:
                
                if r-l+1 < reslen:
                    reslen = r - l + 1
                    res = [l,r]

                sd[s[l]] -= 1

                if s[l] in td and sd[s[l]] < td[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        return s[l:r+ 1] if reslen != float('infinity') else ''


        