from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        q = deque(set())
        maxL = 0

        for r in s:
            
            if r in q:
                while r in q:
                    q.popleft()
            maxL = max(maxL, len(q) + 1)
            q.append(r)
        return maxL
        