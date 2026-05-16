class Solution:
    '''
    input: str
    output: decoded strs == str

    edge cases: empty str, one word

    plan:
    find a way to denote the start and end of a word
    put size of word at the beginning of word and a #to show end of size
    encode: '5#hello5#world7#tod4a4y'
    decode: loop through strs
    use the num in front to figure out length of word
    '''

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs: #O(m)
            length = len(word)
            s += str(length) + '#' + word

        return s

    '''
    strs = ['h5ll0', 'w0rl0']
    s = ''

    word = 'h5ll0'
    length = 5
    s = '5#h5ll0'

    word = 'w0rl0'
    length = 5
    s = '5#h5ll05#w0rl0'
    i = 1
    j = 2
    5 + 1 + 1 = 7
    '''

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):#O(n)
            num = ''
            while s[i] != '#':
                num += s[i]
                i += 1
            
            length = int(num)
            word = ''
            j = i + 1
            # while j < (length + i + 1) and j < len(s):
            #     word += s[j]
            #     j += 1
            word = s[j: length + i + 1]
            i = length + i + 1
            strs.append(word)
        
        return strs


    '''
    Time:O(n)
    Space:O(1)
    '''

    
    

