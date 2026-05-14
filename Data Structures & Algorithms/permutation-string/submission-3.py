class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #put in counter to get frequency
        #use sliding window to compare
        s1c = Counter(s1)
        s2c = Counter()

        for i in range(len(s2)):
            s2c[s2[i]] += 1

            if i >= len(s1):
                unw = i - len(s1)
                if s2c[s2[unw]] == 1:
                    del s2c[s2[unw]]
                elif s2c[s2[unw]] > 1:
                    s2c[s2[unw]] -= 1
            if s1c == s2c:
                return True
        return False
