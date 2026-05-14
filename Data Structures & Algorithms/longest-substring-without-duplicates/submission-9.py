class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_dict = {}
        maxA = 0
        l = 0

        for r in range(len(s)):
            if s[r] in s_dict and s_dict[s[r]] >= l:
                # Move the left pointer only if the repeated character is inside the current window
                l = s_dict[s[r]] + 1
            
            # Update the position of the character
            s_dict[s[r]] = r
            
            # Calculate the maximum length
            maxA = max(maxA, r - l + 1)

        return maxA
