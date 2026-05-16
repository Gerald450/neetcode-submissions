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
        for word in strs:
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

    '''

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            num = ''
            while s[i] != '#':
                num += s[i]
                i += 1
            
            length = int(num)
            word = ''
            j = i + 1
            while j < (length + i + 1) and j < len(s):
                word += s[j]
                j += 1
            i = j
            strs.append(word)
        
        return strs

    '''
    s = '5h5ll05w0rl0'
    strs = []
    i = 0
    i: 0 -> 11

    length = s[0] = 5
    word = ''
    j = 1
        j: 1 -> 6
        word = 'h'
        j = 2
        word = 'h5'
        j= 3
        word = 'h5l'
        j = 4
        word = 'h5ll'
        j = 5
        word = 'h5ll0'
        j = 6
    i = 6
    strs = ['h5ll0']

    length = s[6] = 5
    word = ''
    j = 7
    j: 7 -> 11
    ...
    word = 'w0rl0'
    j = 12

    i = 12
    strs = ['h5ll0', 'w0rl0']
    '''


    

