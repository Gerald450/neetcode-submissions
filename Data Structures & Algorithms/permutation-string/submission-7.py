from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_dict = Counter(s1)
        s2_dict = Counter()

        l = 0

        for r in range(len(s2)):

            s2_dict[s2[r]] = 1 + s2_dict.get(s2[r], 0)

            if r - l + 1 == len(s1):
                if s1_dict != s2_dict:
                    s2_dict[s2[l]] -= 1
                    l += 1
                else:
                    return True
        return False
        