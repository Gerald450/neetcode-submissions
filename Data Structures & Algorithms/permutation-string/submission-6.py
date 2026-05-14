class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict, s2_dict = {}, {}
        s2_set = set()

        for letter in s1:
            s1_dict[letter] = 1 + s1_dict.get(letter, 0)
        l = 0

        for r in range(len(s2)):
            c = s2[r]
            s2_dict[c] = 1 + s2_dict.get(c, 0)

            if (r - l + 1) >= len(s1):
                if s1_dict == s2_dict:
                    return True
                else:
                    if s2_dict[s2[l]] > 1:
                        s2_dict[s2[l]] -= 1
                    else:
                        del s2_dict[s2[l]]
                    l += 1
        return False



