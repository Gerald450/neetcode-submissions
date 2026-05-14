class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == '': return ''
        
        s_dict, t_dict = {}, {}

        for letter in t:
            t_dict[letter] = 1 + t_dict.get(letter, 0)

        res, reslen = [-1,-1], float('infinity')
        l = 0
        have, need = 0 , len(t_dict)

        for r in range(len(s)):
            c = s[r]
            s_dict[c] = 1 + s_dict.get(c, 0)

            if c in t_dict and t_dict[c] == s_dict[c]:
                have += 1
            
            while have == need:


                s_dict[s[l]] -= 1

                if (r - l + 1) < reslen:
                    res = [l,r]
                    reslen = r - l + 1

                if s[l] in t_dict and t_dict[s[l]] > s_dict[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if reslen != float('infinity') else ''

