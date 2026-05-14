class Solution:

    def encode(self, strs: List[str]) -> str:
        coded=''

        for word in strs:
            coded+=str(len(word)) + '#' + word
        
        return coded

    def decode(self, s: str) -> List[str]:

        otp = []

        l = 0
        

        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            otp.append(s[l:r])
            l = r
           

        return otp
   