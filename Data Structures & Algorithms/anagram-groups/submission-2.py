class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        input: array of strings
        output: array of arrays of grouped anagrams
        edge cases: no anagrams, empty input str

        Plan:
            loop through each word
                sort the word, see if it exist in dictionary, save it as a value of that key
                save it as a key(tuple) in a dic and as a value

            return a list of values

        '''
        from collections import defaultdict
        hashmap = defaultdict(list)

        for word in strs:
            w = sorted(word)
            w = tuple(w)

            hashmap[w].append(word)

        return list(hashmap.values())
            
            
